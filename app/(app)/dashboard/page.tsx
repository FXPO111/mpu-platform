export default function DashboardPage() {
  const stats = [
    { name: "Кейсы", value: "3" },
    { name: "Сообщения", value: "48" },
    { name: "Trainer", value: "2 сессии" },
    { name: "Баланс", value: "€0" },
  ];

  const recent = [
    { id: "C-1021", topic: "Алкоголь", updated: "сегодня", status: "draft" },
    { id: "C-1019", topic: "Нарушение", updated: "вчера", status: "in_review" },
    { id: "C-1012", topic: "ДТП", updated: "3 дня назад", status: "ready" },
  ];

  return (
    <div style={{ display: "grid", gap: 16 }}>
      <div className="card pad">
        <div className="badge">Dashboard</div>
        <h1 className="h2" style={{ marginTop: 10 }}>Сводка</h1>
        <p className="p">Статистика и последние кейсы.</p>
      </div>

      <div className="grid2">
        <div className="card pad">
          <h2 className="h2">Показатели</h2>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(2, 1fr)", gap: 12, marginTop: 12 }}>
            {stats.map((s) => (
              <div key={s.name} className="card pad" style={{ boxShadow: "none" }}>
                <div className="badge">{s.name}</div>
                <div style={{ fontSize: 26, fontWeight: 800, marginTop: 10 }}>{s.value}</div>
              </div>
            ))}
          </div>
        </div>

        <div className="card pad">
          <h2 className="h2">Последние кейсы</h2>
          <div className="hr" />
          <div style={{ display: "grid", gap: 10 }}>
            {recent.map((r) => (
              <div key={r.id} className="card pad" style={{ boxShadow: "none" }}>
                <div style={{ display: "flex", justifyContent: "space-between", gap: 10, flexWrap: "wrap" }}>
                  <div>
                    <div style={{ fontWeight: 800 }}>{r.id}</div>
                    <div className="p">{r.topic}</div>
                  </div>
                  <div style={{ textAlign: "right" }}>
                    <div className="badge">{r.status}</div>
                    <div className="p" style={{ marginTop: 6 }}>{r.updated}</div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
