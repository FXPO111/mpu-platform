export default function TrainerPage({ params }: { params: { sessionId: string } }) {
  return <main><h1>Trainer session {params.sessionId}</h1><p>Chat trainer UI should stream messages and show credit usage.</p></main>;
}
