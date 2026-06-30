import { useEffect, useState } from "react";

function App() {
  const [students, setStudents] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/students") // ✅ matches backend route
      .then((response) => response.json())
      .then((data) => {
        setStudents(data);
      });
  }, []);

  return (
    <>
      <h1>React + FastAPI</h1>
      {students.length === 0 ? (
        <p>No students found</p>
      ) : (
        students.map((s) => (
          <div key={s.id}>
            <h2>{s.name}</h2>
            <p>Age: {s.age}</p>
            <p>City: {s.city}</p>
          </div>
        ))
      )}
    </>
  );
}

export default App;
