import express from "express";
import cors from "cors";
import MainRouter from "../routes";

const app = express();
const PORT = process.env.PORT;

app.use(cors());
app.use(express.json());

app.get("/", (_req, res) => {
  return res.json({
    message: "Hello CodeSage!",
  });
});

app.use("/", MainRouter);

app.listen(PORT, () => {
  console.log(`Backend running on PORT: ${PORT}`);
});
