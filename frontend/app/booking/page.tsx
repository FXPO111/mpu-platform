const slots = [
  { day: 'Mon', time: '09:00', type: 'Online consultation' },
  { day: 'Wed', time: '13:30', type: 'Online consultation' },
  { day: 'Fri', time: '10:00', type: 'Online consultation' },
];

export default function BookingPage() {
  return (
    <>
      <section className="hero">
        <span className="tag">Booking</span>
        <h1>Reserve your consultation slot.</h1>
        <p className="muted">Choose an available time. Final booking is confirmed after payment.</p>
      </section>

      <section className="grid grid-3">
        {slots.map((slot) => (
          <article className="card" key={`${slot.day}-${slot.time}`}>
            <h3>
              {slot.day} · {slot.time}
            </h3>
            <p className="muted">{slot.type}</p>
            <a className="btn btn-secondary" href="/login">
              Continue to booking
            </a>
          </article>
        ))}
      </section>
    </>
  );
}
