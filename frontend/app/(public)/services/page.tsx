import Link from "next/link";
import { Button } from "@/components/ui/Button";

export default function ServicesPage() {
  return (
    <div style={{ display: "grid", gap: 16 }}>
      <div className="card pad">
        <div className="badge">Услуги</div>
        <h1 className="h2" style={{ marginTop: 10 }}>Форматы подготовки</h1>
        <p className="p">
          Старт — информационная консультация (30€ / 30 минут), дальше выбираем формат под вашу ситуацию.
        </p>
        <div style={{ marginTop: 12 }}>
          <Link href="/contact"><Button>Записаться</Button></Link>
        </div>
      </div>

      <div className="cards3">
        <div className="card pad soft">
          <div className="badge">Проверка готовности</div>
          <p className="p">Контрольная сессия перед интервью + список исправлений.</p>
        </div>
        <div className="card pad soft">
          <div className="badge">Анализ неудачной попытки</div>
          <p className="p">Разбор отчёта и сценария отказа + план повторной сдачи.</p>
        </div>
        <div className="card pad soft">
          <div className="badge">Подготовка к MPU</div>
          <p className="p">Полная индивидуальная подготовка: стратегия, документы, тренировка.</p>
        </div>
      </div>
    </div>
  );
}
