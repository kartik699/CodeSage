import express from "express";
import cors from "cors";

const app = express();

app.use(cors());
app.use(express.json());

const PORT = process.env.PORT;

app.get("/health", (_req, res) => {
  return res.json({
    status: "backend ok (bun)",
  });
});

app.listen(PORT, () => {
  console.log(`Backend running on PORT: ${PORT}`);
});
