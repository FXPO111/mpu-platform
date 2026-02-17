export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body style={{ fontFamily: 'sans-serif', maxWidth: 900, margin: '0 auto', padding: 24 }}>
        <nav style={{ display: 'flex', gap: 16, marginBottom: 24 }}>
          <a href="/">Home</a><a href="/pricing">Pricing</a><a href="/expert">Expert</a><a href="/booking">Booking</a><a href="/dashboard">Dashboard</a>
        </nav>
        {children}
      </body>
    </html>
  );
}
