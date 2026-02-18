export default function LandingPage() {
  return (
    <>
      <section className="hero">
        <span className="tag">AI + Expert workflow</span>
        <h1>Pass MPU with a focused training system, not random chat.</h1>
        <p className="muted">
          Start with a diagnostic interview, get rubric-based feedback, and book your live consultation in one flow.
          Built for remote clients across cities.
        </p>
        <div className="actions">
          <a className="btn btn-primary" href="/login">
            Start diagnostic
          </a>
          <a className="btn btn-secondary" href="/pricing">
            View pricing
          </a>
        </div>
      </section>

      <section className="grid grid-3">
        <article className="card">
          <h3>Diagnostic mode</h3>
          <p className="muted">Find weak rubrics and get a 7-day practice plan from your first session.</p>
        </article>
        <article className="card">
          <h3>Practice mode</h3>
          <p className="muted">Adaptive questions target weak topics and measure your progress session by session.</p>
        </article>
        <article className="card">
          <h3>Consultations</h3>
          <p className="muted">Book online slots, track status in dashboard, and prepare with context in one place.</p>
        </article>
      </section>

      <section className="panel">
        <h2>What makes this different</h2>
        <ul className="list">
          <li>Structured rubric scoring (clarity, responsibility, consistency)</li>
          <li>Credit-based AI access + separate consultation booking flow</li>
          <li>Stripe webhook-based access management</li>
        </ul>
      </section>
    </>
  );
}
