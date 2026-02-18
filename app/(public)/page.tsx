import Link from "next/link";
import { Button } from "@/components/ui/Button";

export default function HomePage() {
  return (
    <div style={{ display: "grid", gap: 18 }}>
      {/* HERO */}
      <section className="section">
        <div className="hero-grid">
          <div className="card pad hero-main">
            <div className="badge">MPU AI • подготовка и консультации</div>

            <h1 className="h1" style={{ marginTop: 14 }}>
              Подготовка к MPU как система: диагностика → план → тренировка интервью
            </h1>

            <p className="p" style={{ marginTop: 12, fontSize: 16 }}>
              ИИ собирает факты по вашему кейсу, строит персональный план и прогоняет через симуляцию интервью.
              Если риск высокий — предложит созвон с экспертом (Zoom).
            </p>

            <div className="chips">
              <span className="chip">конфиденциально</span>
              <span className="chip">структура реального интервью</span>
              <span className="chip">история и прогресс в кабинете</span>
              <span className="chip">эскалация к эксперту по триггерам</span>
            </div>

            <div className="hero-actions">
              <Link href="/start"><Button size="lg">Начать диагностику</Button></Link>
              <Link href="/booking"><Button size="lg" variant="secondary">Записаться к эксперту</Button></Link>
              <Link href="/pricing"><Button size="lg" variant="ghost">Тарифы</Button></Link>
            </div>
          </div>

          <div className="card pad hero-side">
            <div className="badge">Что вы получите</div>

            <div className="hr" />

            <div style={{ display: "grid", gap: 12 }}>
              <div className="card pad soft">
                <div className="badge">Персональный план</div>
                <p className="p" style={{ marginTop: 8 }}>
                  Что говорить, что подтверждать документами, где слабые места, что подготовить заранее.
                </p>
              </div>

              <div className="card pad soft">
                <div className="badge">Trainer-интервью</div>
                <p className="p" style={{ marginTop: 8 }}>
                  Симуляция вопросов, follow-up, оценка ответов, рекомендации как исправить формулировки.
                </p>
              </div>

              <div className="card pad soft">
                <div className="badge">Триггеры на Zoom</div>
                <p className="p" style={{ marginTop: 8 }}>
                  Если кейс “красный” — система предложит консультацию и сформирует список вопросов эксперту.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* HOW IT WORKS */}
      <section className="section">
        <div className="section-head">
          <div>
            <div className="badge">Как работает</div>
            <h2 className="h2" style={{ marginTop: 10 }}>Флоу, который ведёт к результату</h2>
          </div>
          <Link href="/how-it-works"><Button variant="ghost">Подробнее</Button></Link>
        </div>

        <div className="steps">
          <div className="faq-item">
            <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
              <span className="step-num">1</span>
              <p className="faq-q">Диагностика</p>
            </div>
            <p className="faq-a">Сбор фактов: причина, сроки, поведение после случая, терапия/курсы, документы.</p>
          </div>

          <div className="faq-item">
            <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
              <span className="step-num">2</span>
              <p className="faq-q">План</p>
            </div>
            <p className="faq-a">Структура истории, чек-лист доказательств изменений, список рисков и действий.</p>
          </div>

          <div className="faq-item">
            <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
              <span className="step-num">3</span>
              <p className="faq-q">Тренировка</p>
            </div>
            <p className="faq-a">Интервью-симуляция: вопросы, follow-up, рекомендации по формулировкам.</p>
          </div>

          <div className="faq-item">
            <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
              <span className="step-num">4</span>
              <p className="faq-q">Эксперт</p>
            </div>
            <p className="faq-a">Если риск высокий — Zoom, запись, подготовленные системой вопросы и документы.</p>
          </div>
        </div>
      </section>

      {/* FEATURES */}
      <section className="section">
        <div className="badge">Для чего это</div>
        <h2 className="h2" style={{ marginTop: 10 }}>Закрываем типовые причины провала</h2>

        <div className="features">
          <div className="card pad soft">
            <div className="badge">Нет структуры рассказа</div>
            <p className="p" style={{ marginTop: 8 }}>
              ИИ выстраивает хронологию и “смысл” изменений, чтобы ответы звучали логично и доказуемо.
            </p>
          </div>

          <div className="card pad soft">
            <div className="badge">Слабые доказательства</div>
            <p className="p" style={{ marginTop: 8 }}>
              Чек-лист документов/действий: что подтвердить, как и чем, чтобы не было дыр.
            </p>
          </div>

          <div className="card pad soft">
            <div className="badge">Провал на follow-up</div>
            <p className="p" style={{ marginTop: 8 }}>
              Trainer давит уточняющими вопросами — так же, как на реальном интервью.
            </p>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="section">
        <div className="card pad cta">
          <div className="badge">Старт</div>
          <h2 className="h2" style={{ marginTop: 10 }}>
            Начать можно сейчас — 10–15 минут на диагностику
          </h2>
          <p className="p" style={{ marginTop: 10 }}>
            Дальше система сама предложит: план, тренер, или консультацию в Zoom если кейс рискованный.
          </p>

          <div className="hero-actions">
            <Link href="/start"><Button size="lg">Начать диагностику</Button></Link>
            <Link href="/pricing"><Button size="lg" variant="secondary">Посмотреть тарифы</Button></Link>
          </div>
        </div>
      </section>

      {/* FAQ */}
      <section className="section">
        <div className="badge">FAQ</div>
        <h2 className="h2" style={{ marginTop: 10 }}>Коротко о важном</h2>

        <div className="faq">
          <div className="faq-item">
            <p className="faq-q">ИИ заменяет эксперта?</p>
            <p className="faq-a">
              Нет. Он систематизирует кейс, строит план и тренирует интервью. Эксперт подключается по триггерам риска.
            </p>
          </div>

          <div className="faq-item">
            <p className="faq-q">Можно начать без документов?</p>
            <p className="faq-a">
              Да. Диагностика стартует с фактов, а дальше система выдаст список, что нужно собрать.
            </p>
          </div>

          <div className="faq-item">
            <p className="faq-q">Как это выглядит в кабинете?</p>
            <p className="faq-a">
              Кейсы, прогресс, план, файлы, тренировки, история. Всё по одному делу — в одном месте.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}
