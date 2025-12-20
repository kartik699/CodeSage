import { Router } from "express";
import { sendToAgent } from "../controllers";
import { addRepoPath } from "../middlewares/agentMiddleware";

const router = Router();

router.post("/chat", addRepoPath, sendToAgent);

export default router;
