import type { ReactNode } from "react";
import Link from "next/link";
import { NavLink } from "@/components/nav/NavLink";
import { Button } from "@/components/ui/Button";

export default function PublicLayout({ children }: { children: ReactNode }) {
  return (
    <>
      <header className="public-header">
        <div className="topstrip">
          <div className="container topstrip-inner">
            <span>96% клиентов сдают с первого раза</span>
            <a href="mailto:info@mpu-praxis-dp.de">info@mpu-praxis-dp.de</a>
          </div>
        </div>

        <div className="container public-header-inner">
          <Link href="/" className="brand">
            <span className="brand-dot" />
            MPU AI
          </Link>

          <nav className="nav">
            <NavLink href="/" exact>Главная</NavLink>
            <NavLink href="/services" exact>Услуги</NavLink>
            <NavLink href="/about" exact>Обо мне</NavLink>
            <NavLink href="/contact" exact>Контакты</NavLink>
          </nav>

          <div style={{ display: "flex", gap: 10, alignItems: "center" }}>
            <a href="tel:+491752730963">
              <Button variant="ghost" size="sm">Позвонить</Button>
            </a>
            <Link href="/login">
              <Button variant="secondary" size="sm">Войти</Button>
            </Link>
            <Link href="/dashboard">
              <Button size="sm">Кабинет</Button>
            </Link>
          </div>
        </div>
      </header>

      <main className="container page">{children}</main>

      <footer className="container footer">
        <div className="footer-grid">
          <div>
            <div className="badge">Контакты</div>
            <div className="p" style={{ marginTop: 10 }}>
              <a href="tel:+491752730963">+49 175 27 30 963</a><br />
              <a href="mailto:info@mpu-praxis-dp.de">info@mpu-praxis-dp.de</a>
            </div>
            <div className="p" style={{ marginTop: 10 }}>
              Viktoriastraße 32-36, 56068 Koblenz
            </div>
          </div>

          <div>
            <div className="badge">Навигация</div>
            <div style={{ display: "grid", gap: 8, marginTop: 10 }}>
              <Link className="navlink" href="/services">Услуги</Link>
              <Link className="navlink" href="/about">Обо мне</Link>
              <Link className="navlink" href="/contact">Контакты</Link>
            </div>
          </div>

          <div>
            <div className="badge">Юридическое</div>
            <div style={{ display: "grid", gap: 8, marginTop: 10 }}>
              <Link className="navlink" href="/impressum">Impressum</Link>
              <Link className="navlink" href="/privacy">Datenschutz</Link>
            </div>
          </div>
        </div>

        <div className="footer-bottom">
          © {new Date().getFullYear()} MPU AI • Praxis DP
        </div>
      </footer>
    </>
  );
}
