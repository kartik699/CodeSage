import path from "path";
import type { Request, Response, NextFunction } from "express";

export const addRepoPath = (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  const repoPath = path.resolve(__dirname, "..", "..");

  req.body.repoPath = repoPath;

  next();
};
