import Link from "next/link";
import { Button } from "@/components/ui/Button";

function PlanCard({
  title,
  price,
  desc,
  items,
  cta,
  primary,
}: {
  title: string;
  price: string;
  desc: string;
  items: string[];
  cta: string;
  primary?: boolean;
}) {
  return (
    <div className="card pad" style={{ borderColor: primary ? "rgba(250,204,21,.30)" : undefined }}>
      <div className="badge">{title}</div>
      <div style={{ fontSize: 34, fontWeight: 800, marginTop: 10 }}>{price}</div>
      <p className="p" style={{ marginTop: 8 }}>{desc}</p>

      <div className="hr" />

      <ul style={{ margin: 0, paddingLeft: 18, color: "var(--muted)", lineHeight: 1.7 }}>
        {items.map((x) => <li key={x}>{x}</li>)}
      </ul>

      <div style={{ marginTop: 16 }}>
        <Link href="/login">
          <Button variant={primary ? "primary" : "secondary"} style={{ width: "100%" }}>
            {cta}
          </Button>
        </Link>
      </div>
    </div>
  );
}

export default function PricingPage() {
  return (
    <div>
      <h1 className="h1">Тарифы</h1>
      <p className="p">MVP: пакеты попыток. Подписку и биллинг — следующим шагом.</p>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: 16, marginTop: 18 }}
           className="pricing-grid">
        <PlanCard
          title="Start"
          price="€19"
          desc="Пробный прогон под 1 кейс."
          items={["1 кейс", "До 30 сообщений", "Базовые подсказки", "История 7 дней"]}
          cta="Взять Start"
        />
        <PlanCard
          title="Pro"
          price="€49"
          desc="Нормальная работа в кабинете."
          items={["До 5 кейсов", "До 200 сообщений", "Trainer-сессии", "История 30 дней"]}
          cta="Взять Pro"
          primary
        />
        <PlanCard
          title="Team"
          price="€99"
          desc="Если будет поток клиентов."
          items={["До 20 кейсов", "До 800 сообщений", "Файлы/документы", "Приоритетная очередь"]}
          cta="Взять Team"
        />
      </div>

      <style>{`
        @media (max-width: 980px){
          .pricing-grid{ grid-template-columns: 1fr !important; }
        }
      `}</style>
    </div>
  );
}
