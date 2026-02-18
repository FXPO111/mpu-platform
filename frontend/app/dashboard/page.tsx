export default function DashboardPage() {
  return (
    <>
      <section className="hero">
        <span className="tag">Personal dashboard</span>
        <h1>Your preparation cockpit</h1>
        <p className="muted">Track AI credits, recent sessions and upcoming bookings at a glance.</p>
      </section>

      <section className="grid grid-3">
        <article className="kpi">
          <p className="muted">AI credits left</p>
          <p className="stat">49</p>
        </article>
        <article className="kpi">
          <p className="muted">Latest rubric score</p>
          <p className="stat badge-ok">3.8 / 5</p>
        </article>
        <article className="kpi">
          <p className="muted">Next booking</p>
          <p className="stat">Fri 10:00</p>
        </article>
      </section>

      <section className="grid grid-2">
        <article className="card">
          <h3>Recent sessions</h3>
          <ul className="list">
            <li>Diagnostic session · completed</li>
            <li>Practice block: clarity rubric</li>
            <li>Mock interview warmup</li>
          </ul>
        </article>
        <article className="card">
          <h3>Action items</h3>
          <ul className="list">
            <li>Train consistency follow-up questions</li>
            <li>Prepare 3 concrete behavior-change examples</li>
            <li>Book a review call for final mock</li>
          </ul>
        </article>
      </section>
    </>
  );
}
