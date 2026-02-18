export default function AdminPage() {
  return (
    <>
      <section className="hero">
        <span className="tag">Admin zone</span>
        <h1>Operations panel</h1>
        <p className="muted">Manage catalog data, slots, and quality controls from one workspace.</p>
      </section>

      <section className="grid grid-3">
        <article className="card">
          <h3>Content</h3>
          <p className="muted">Topics, questions, rubrics, and materials.</p>
        </article>
        <article className="card">
          <h3>Products</h3>
          <p className="muted">AI packs, consultation offers, and active pricing.</p>
        </article>
        <article className="card">
          <h3>Slots</h3>
          <p className="muted">Open slots, meeting URLs, and booking states.</p>
        </article>
      </section>
    </>
  );
}
