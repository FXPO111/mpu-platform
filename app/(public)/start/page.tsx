"use client";

import { useMemo, useState } from "react";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";

const STEPS = [
  { k: "reason", title: "Причина MPU", hint: "Алкоголь / наркотики / баллы / агрессия / другое" },
  { k: "timeline", title: "Хронология", hint: "Когда произошло, что было дальше, сроки" },
  { k: "changes", title: "Изменения", hint: "Что изменили: терапия, курсы, анализы, поведение" },
  { k: "docs", title: "Документы", hint: "Что есть на руках, чего нет" },
];

export default function StartPage() {
  const [i, setI] = useState(0);
  const [data, setData] = useState<Record<string, string>>({});

  const step = STEPS[i];
  const value = data[step.k] ?? "";

  const canNext = value.trim().length >= 8;

  const progress = useMemo(() => Math.round(((i + 1) / STEPS.length) * 100), [i]);

  return (
    <div style={{ display: "grid", gap: 16 }}>
      <div className="card pad">
        <div className="badge">Диагностика • шаг {i + 1}/{STEPS.length} • {progress}%</div>
        <h1 className="h2" style={{ marginTop: 10 }}>{step.title}</h1>
        <p className="p" style={{ marginTop: 8 }}>{step.hint}</p>

        <div style={{ marginTop: 12 }}>
          <Input
            placeholder="Введите кратко, но по сути"
            value={value}
            onChange={(e) => setData((p) => ({ ...p, [step.k]: e.target.value }))}
          />
        </div>

        <div style={{ display: "flex", gap: 10, marginTop: 14 }}>
          <Button
            variant="ghost"
            disabled={i === 0}
            onClick={() => setI((v) => Math.max(0, v - 1))}
          >
            Назад
          </Button>

          {i < STEPS.length - 1 ? (
            <Button disabled={!canNext} onClick={() => setI((v) => Math.min(STEPS.length - 1, v + 1))}>
              Далее
            </Button>
          ) : (
            <Button
              disabled={!canNext}
              onClick={() => {
                // пока MVP: просто сохраняем локально
                localStorage.setItem("mpu_draft", JSON.stringify(data));
                alert("Черновик сохранён. Следующий шаг: генерация плана и создание кейса в кабинете.");
              }}
            >
              Сформировать черновик
            </Button>
          )}
        </div>
      </div>

      <div className="card pad soft">
        <div className="badge">Что будет дальше</div>
        <p className="p" style={{ marginTop: 10 }}>
          После диагностики система построит план, предложит тренировку интервью и при необходимости — запись к эксперту (Zoom).
        </p>
      </div>
    </div>
  );
}
