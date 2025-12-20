export interface AgentResponse {
  result: string;
  numFiles?: number;
  filesChecked?: string[];
}

export interface ExpressResponse {
  code: number;
  data: AgentResponse;
}
