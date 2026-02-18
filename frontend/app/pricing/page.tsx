const plans = [
  {
    name: 'AI Pack 50',
    price: '€49',
    note: 'Great for first diagnostic + quick practice cycle.',
  },
  {
    name: 'AI Pack 150',
    price: '€99',
    note: 'Balanced option for multi-week preparation.',
  },
  {
    name: 'Consultation 60 min',
    price: '€99',
    note: 'Live session with expert and action plan review.',
  },
];

export default function PricingPage() {
  return (
    <>
      <section className="hero">
        <span className="tag">Transparent pricing</span>
        <h1>Choose the pace of your MPU preparation.</h1>
        <p className="muted">Buy AI credits for daily progress or book a live strategy call with the specialist.</p>
      </section>

      <section className="grid grid-3">
        {plans.map((plan) => (
          <article className="card" key={plan.name}>
            <h3>{plan.name}</h3>
            <p className="stat">{plan.price}</p>
            <p className="muted">{plan.note}</p>
            <a className="btn btn-secondary" href="/login">
              Continue
            </a>
          </article>
        ))}
      </section>
    </>
  );
}
