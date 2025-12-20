"use client";

import axios from "axios";
import { useState } from "react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { AgentResponse, ExpressResponse } from "@/models/agentResponse";

export default function Home() {
  const [query, setQuery] = useState<string>("");
  const [agentResponse, setAgentResponse] = useState<AgentResponse>();

  const submitQuery = async () => {
    if (!query.trim()) {
      console.log("query is required!");
      setAgentResponse(undefined);
      return;
    }

    try {
      const res = await axios.post<ExpressResponse>(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/chat`,
        {
          ques: query,
          repoPath: "a/b/c/d/e",
        }
      );

      if (res.status === 200) {
        setAgentResponse(res.data.data);
      }
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <main className="p-5">
      <h1 className="text-4xl font-bold">CodeSage</h1>
      <p>Understand any codebase, intelligently.</p>

      <Label htmlFor="user-query" className="mt-4 mb-2">
        Ask your query
      </Label>
      <Input
        id="user-query"
        type="text"
        placeholder="Example - Where is Auth handled?"
        className="mb-2"
        onChange={(e) => setQuery(e.target.value)}
      ></Input>
      <Button
        variant="default"
        className="cursor-pointer"
        onClick={submitQuery}
      >
        Ask
      </Button>
      {agentResponse && (
        <div className="mt-4">
          <span>AI: {agentResponse.result}</span>
          <br></br>
          <span>Number of Files Read: {agentResponse.numFiles ?? 0}</span>
          <br></br>
          <span>
            List of Files Read:{" "}
            {agentResponse.filesChecked && agentResponse.filesChecked.length > 0
              ? agentResponse.filesChecked.join(",")
              : "No Files Read"}
          </span>
        </div>
      )}
    </main>
  );
}
