"""
verificar-token-meta.py — Verifica validade do token Meta e envia alerta por e-mail.

Executa diariamente via Task Scheduler. Envia e-mail apenas quando o token estiver
a DIAS_ALERTA dias ou menos de expirar — evita spam em dias normais.

Credenciais necessárias em credentials/ (raiz do projeto):
  meta_token_expira_em.txt  — data de expiração do token: AAAA-MM-DD
  gmail_remetente.txt       — e-mail remetente (Gmail com App Password configurado)
  gmail_app_password.txt    — senha de app do Gmail (não a senha normal da conta)
  gmail_destinatarios.txt   — destinatários separados por vírgula

Como gerar a App Password do Gmail:
  1. Ative a verificação em 2 etapas em myaccount.google.com/security
  2. Acesse myaccount.google.com/apppasswords
  3. Crie uma senha para "Outro (nome personalizado)" → "LeAnge Content"
  4. Copie os 16 caracteres e salve em credentials/gmail_app_password.txt
"""

import smtplib
import sys
from datetime import date, datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

# Este script fica em .claude/skills/publicar-social-leange/ — 4 níveis abaixo da raiz
CREDENTIALS_DIR = Path(__file__).parent.parent.parent.parent / "credentials"

# Quantos dias antes do vencimento o alerta começa a ser enviado
DIAS_ALERTA = 10


def ler_credencial(nome: str) -> str:
    caminho = CREDENTIALS_DIR / nome
    if not caminho.exists():
        print(f"ERRO: credentials/{nome} não encontrado.", file=sys.stderr)
        sys.exit(2)
    valor = caminho.read_text(encoding="utf-8").strip()
    if not valor or valor.startswith("PREENCHER"):
        print(f"ERRO: credentials/{nome} não foi preenchido.", file=sys.stderr)
        sys.exit(2)
    return valor


def main():
    # Ler e validar data de expiração
    data_str = ler_credencial("meta_token_expira_em.txt")
    try:
        expira_em = datetime.strptime(data_str, "%Y-%m-%d").date()
    except ValueError:
        print(f"ERRO: formato inválido em meta_token_expira_em.txt. Use AAAA-MM-DD.", file=sys.stderr)
        sys.exit(1)

    hoje = date.today()
    dias_restantes = (expira_em - hoje).days

    print(f"Token Meta — expira em: {expira_em.strftime('%d/%m/%Y')} ({dias_restantes} dias restantes)")

    # Só envia e-mail quando estiver perto do vencimento
    if dias_restantes > DIAS_ALERTA:
        print(f"OK — token válido. Nenhum alerta necessário.")
        return

    # Definir urgência da mensagem
    if dias_restantes < 0:
        assunto = "🚨 Token Meta EXPIRADO — publicação no Instagram parada"
        situacao = f"O token <strong>já expirou</strong> em {expira_em.strftime('%d/%m/%Y')}. A publicação automática no Instagram está fora do ar."
        cor_header = "#c0392b"
    elif dias_restantes == 0:
        assunto = "🚨 Token Meta expira HOJE — renovar agora"
        situacao = "O token <strong>expira hoje</strong>. Renove imediatamente para não interromper as publicações."
        cor_header = "#c0392b"
    else:
        assunto = f"⚠️ Token Meta expira em {dias_restantes} dias — renovar antes de {expira_em.strftime('%d/%m/%Y')}"
        situacao = f"O token expira em <strong>{dias_restantes} dias</strong> ({expira_em.strftime('%d/%m/%Y')}). Renove com antecedência."
        cor_header = "#e67e22"

    # Montar e-mail
    remetente = ler_credencial("gmail_remetente.txt")
    app_password = ler_credencial("gmail_app_password.txt")
    destinatarios = [e.strip() for e in ler_credencial("gmail_destinatarios.txt").split(",")]

    corpo_html = f"""
<!DOCTYPE html>
<html>
<body style="font-family: Arial, sans-serif; background: #f5f5f5; margin: 0; padding: 20px;">
  <div style="max-width: 560px; margin: 0 auto; background: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">

    <div style="background: {cor_header}; padding: 24px 32px;">
      <h2 style="color: #fff; margin: 0; font-size: 18px;">{assunto}</h2>
    </div>

    <div style="padding: 32px;">
      <p style="font-size: 16px; color: #333; margin-top: 0;">{situacao}</p>

      <hr style="border: none; border-top: 1px solid #eee; margin: 24px 0;">

      <h3 style="color: #333; font-size: 15px;">Como renovar o token:</h3>
      <ol style="color: #555; font-size: 14px; line-height: 1.8;">
        <li>Acesse <a href="https://developers.facebook.com/tools/explorer" style="color: #2980b9;">developers.facebook.com/tools/explorer</a></li>
        <li>Selecione o app <strong>LeAnge Content</strong> e gere um novo token com as permissões:<br>
            <code style="background: #f0f0f0; padding: 2px 6px; border-radius: 3px; font-size: 12px;">
              instagram_content_publish, pages_show_list, pages_read_engagement, instagram_basic
            </code>
        </li>
        <li>Converta para <strong>long-lived token</strong> (válido 60 dias) via Graph API Explorer:<br>
            <code style="background: #f0f0f0; padding: 4px 8px; border-radius: 3px; font-size: 12px; display: block; margin-top: 6px;">
              GET /oauth/access_token?grant_type=fb_exchange_token
              &amp;client_id={{APP_ID}}&amp;client_secret={{APP_SECRET}}
              &amp;fb_exchange_token={{TOKEN_CURTO}}
            </code>
        </li>
        <li>Salve o novo token em <code style="background: #f0f0f0; padding: 2px 6px; border-radius: 3px; font-size: 12px;">credentials/meta_access_token.txt</code></li>
        <li>Atualize a nova data de expiração em <code style="background: #f0f0f0; padding: 2px 6px; border-radius: 3px; font-size: 12px;">credentials/meta_token_expira_em.txt</code> (formato: AAAA-MM-DD)</li>
      </ol>

      <p style="font-size: 13px; color: #999; margin-bottom: 0; border-top: 1px solid #eee; padding-top: 16px;">
        Alerta automático — LeAnge Content · Conta: [empresa] Instagram
      </p>
    </div>
  </div>
</body>
</html>
"""

    msg = MIMEMultipart("alternative")
    msg["Subject"] = assunto
    msg["From"] = remetente
    msg["To"] = ", ".join(destinatarios)
    msg.attach(MIMEText(corpo_html, "html", "utf-8"))

    print(f"Enviando alerta para: {', '.join(destinatarios)}...")
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(remetente, app_password)
            smtp.sendmail(remetente, destinatarios, msg.as_string())
        print("OK — alerta enviado com sucesso.")
    except smtplib.SMTPAuthenticationError:
        print("ERRO: autenticação Gmail falhou.", file=sys.stderr)
        print("  Verifique se credentials/gmail_app_password.txt contém uma App Password válida.", file=sys.stderr)
        print("  App Password ≠ senha normal do Gmail. Gere em: myaccount.google.com/apppasswords", file=sys.stderr)
        sys.exit(3)
    except Exception as e:
        print(f"ERRO ao enviar e-mail: {e}", file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    main()
