import { Router } from "express";

import HealthRouter from "./health";
import AgentRouter from "./agent";

const router = Router();

router.use("/", HealthRouter);
router.use("/", AgentRouter);

export default router;
