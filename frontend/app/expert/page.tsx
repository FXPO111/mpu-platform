export default function ExpertPage() {
  return (
    <>
      <section className="hero">
        <span className="tag">Your consultant</span>
        <h1>Certified MPU specialist, focused on interview readiness.</h1>
        <p className="muted">
          Language support: DE / EN. Online-first support with structured feedback, contradiction checks and
          interview framing.
        </p>
        <div className="actions">
          <a className="btn btn-primary" href="/booking">
            Book a session
          </a>
        </div>
      </section>

      <section className="grid grid-2">
        <article className="card">
          <h3>Specialization</h3>
          <ul className="list">
            <li>MPU interview narrative structure</li>
            <li>Risk responsibility and consistency coaching</li>
            <li>Behavior-change evidence preparation</li>
          </ul>
        </article>
        <article className="card">
          <h3>How sessions work</h3>
          <ul className="list">
            <li>Pre-session context review from AI training history</li>
            <li>Targeted mock blocks with direct feedback</li>
            <li>Post-session action checklist</li>
          </ul>
        </article>
      </section>
    </>
  );
}
