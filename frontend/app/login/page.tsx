export default function LoginPage() {
  return (
    <section className="grid grid-2">
      <article className="card">
        <h1>Welcome back</h1>
        <p className="muted">Sign in to continue your training and booking flow.</p>
        <label>
          Email
          <input className="input" type="email" placeholder="you@example.com" />
        </label>
        <label>
          Password
          <input className="input" type="password" placeholder="••••••••••" />
        </label>
        <div className="actions">
          <button className="btn btn-primary" type="button">
            Sign in
          </button>
        </div>
      </article>

      <article className="card">
        <h2>Create account</h2>
        <p className="muted">New to the platform? Register and start diagnostic mode in minutes.</p>
        <label>
          Full name
          <input className="input" type="text" placeholder="Max Mustermann" />
        </label>
        <label>
          Locale
          <select className="select" defaultValue="de">
            <option value="de">Deutsch</option>
            <option value="en">English</option>
          </select>
        </label>
        <div className="actions">
          <button className="btn btn-secondary" type="button">
            Create account
          </button>
        </div>
      </article>
    </section>
  );
}
