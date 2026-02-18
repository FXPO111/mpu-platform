import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";

export default function TrainerSessionPage({ params }: { params: { sessionId: string } }) {
  return (
    <div style={{ display: "grid", gap: 16 }}>
      <div className="card pad">
        <div className="badge">Trainer session</div>
        <h1 className="h2" style={{ marginTop: 10 }}>Сессия: {params.sessionId}</h1>
        <p className="p">
          Здесь будет “интервью”-режим: вопрос → твой ответ → разбор → следующая итерация.
        </p>
      </div>

      <div className="card pad">
        <div style={{ display: "flex", gap: 10 }}>
          <Input placeholder="Напиши ответ…" />
          <Button>Отправить</Button>
        </div>

        <div className="hr" />

        <div style={{ display: "grid", gap: 10 }}>
          <div className="card pad" style={{ boxShadow: "none" }}>
            <div className="badge">Эксперт</div>
            <p className="p" style={{ marginTop: 8 }}>
              Вопрос: почему вы считаете, что риск повторения устранён?
            </p>
          </div>

          <div className="card pad" style={{ boxShadow: "none" }}>
            <div className="badge">Вы</div>
            <p className="p" style={{ marginTop: 8 }}>
              (пример ответа — будет подставляться из формы)
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
