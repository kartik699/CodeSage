from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated, List, Optional, Union
import operator

class AgentState(TypedDict):
    messages: Annotated[List[AnyMessage], operator.add]
    final_result: Optional[dict[str, Union[str, int, list[str]]]]