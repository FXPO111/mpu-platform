"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { cn } from "../ui/cn";

export function NavLink({
  href,
  children,
  exact,
  className,
}: {
  href: string;
  children: React.ReactNode;
  exact?: boolean;
  className?: string;
}) {
  const p = usePathname() || "/";
  const active = exact ? p === href : (p === href || p.startsWith(href + "/"));
  return (
    <Link href={href} className={cn("navlink", active && "active", className)}>
      {children}
    </Link>
  );
}
