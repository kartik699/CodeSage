import type { Request, Response } from "express";

export const healthCheck = async (_req: Request, res: Response) => {
  return res.status(200).json({
    status: "backend ok (bun)",
  });
};
