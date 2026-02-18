"use client";

import type { ReactNode } from "react";
import Link from "next/link";
import { NavLink } from "@/components/nav/NavLink";
import { Input } from "@/components/ui/Input";
import { Button } from "@/components/ui/Button";

export default function AppLayout({ children }: { children: ReactNode }) {
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand" style={{ marginBottom: 14 }}>
          <span className="brand-dot" />
          <Link href="/dashboard">MPU AI</Link>
        </div>

        <div className="box">
          <div className="badge">Баланс: 0 • План: MVP</div>
          <div className="sidebar-nav">
            <NavLink href="/dashboard" exact>
              Dashboard
            </NavLink>
            <NavLink href="/booking" exact>
              Booking
            </NavLink>
            <NavLink href="/trainer" exact>
              Trainer
            </NavLink>
            <NavLink href="/admin" exact>
              Admin
            </NavLink>
          </div>

          <div className="hr" />

          <Link href="/pricing">
            <Button variant="primary" size="sm" style={{ width: "100%" }}>
              Пополнить / Тарифы
            </Button>
          </Link>
        </div>
      </aside>

      <div>
        <div className="topbar">
          <div className="container topbar-inner">
            <div style={{ width: "min(520px, 100%)" }}>
              <Input placeholder="Поиск по кейсам, пользователям, сессиям…" />
            </div>
            <div style={{ display: "flex", gap: 10, alignItems: "center" }}>
              <span className="badge">user@mpu</span>
              <Button variant="ghost" size="sm">
                Выход
              </Button>
            </div>
          </div>
        </div>

        <div className="content">
          <div className="container page">{children}</div>
        </div>
      </div>
    </div>
  );
}
