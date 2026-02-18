import './globals.css';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <div className="shell">
          <header className="topbar">
            <a className="logo" href="/">
              MPU Platform
            </a>
            <nav className="nav">
              <a href="/">Home</a>
              <a href="/pricing">Pricing</a>
              <a href="/expert">Expert</a>
              <a href="/booking">Booking</a>
              <a href="/dashboard">Dashboard</a>
              <a href="/admin">Admin</a>
            </nav>
          </header>

          <main className="page">{children}</main>

          <footer className="footer">DE/EN-first MPU preparation experience · Built for online-first growth</footer>
        </div>
      </body>
    </html>
  );
}
