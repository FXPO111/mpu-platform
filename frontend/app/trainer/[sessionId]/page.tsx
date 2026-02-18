export default function TrainerPage({ params }: { params: { sessionId: string } }) {
  return (
    <>
      <section className="hero">
        <span className="tag">AI trainer</span>
        <h1>Session {params.sessionId}</h1>
        <p className="muted">Interactive interview rehearsal with rubric scoring and contradiction checks.</p>
      </section>

      <section className="grid grid-2">
        <article className="card">
          <h3>Conversation</h3>
          <p className="muted">Message stream placeholder (user + assistant turns).</p>
          <div className="actions">
            <button className="btn btn-primary" type="button">
              Send message
            </button>
            <button className="btn btn-secondary" type="button">
              Close session
            </button>
          </div>
        </article>

        <article className="card">
          <h3>Live feedback</h3>
          <ul className="list">
            <li>Clarity: 3 / 5</li>
            <li>Consistency: 2 / 5</li>
            <li>Responsibility: 4 / 5</li>
          </ul>
          <p className="muted">
            Credits used: <strong className="badge-alert">1</strong>
          </p>
        </article>
      </section>
    </>
  );
}
