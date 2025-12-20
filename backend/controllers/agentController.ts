import type { Request, Response } from "express";
import axios from "axios";
import type { Payload } from "../models/payload";
import type { AgentResponse } from "../models/agentResponse";

const baseUrl = process.env.AGENT_URL;

export const sendToAgent = async (req: Request, res: Response) => {
  const body = req.body as Payload;
  const { ques, repoPath } = body;

  console.log(ques, repoPath);

  if (!ques || !repoPath) {
    return res.status(404).json({
      code: 404,
      message: "Both question and repo path must be specified",
    });
  }

  try {
    const agentRes = await axios.post<AgentResponse>(`${baseUrl}/chat`, {
      ques,
      repoPath,
    });

    return res.status(200).json({
      code: 200,
      data: agentRes.data,
    });
  } catch (err: any) {
    return res.status(500).json({
      code: 500,
      message: `Internal Server Error - ${err.message}`,
    });
  }
};
