# Dynamo Validation Change Report

Date: 2026-04-13 UTC

This report summarizes the source-tree changes identified while validating RL training against the Dynamo SGLang path in `LLM360/nvidia-dynamo`.

## 1. SGLang chat logprobs forwarding

Problem:
- SGLang worker output contained token logprob information, but the Dynamo path did not consistently forward it through the worker handler and frontend chat formatting path.

Observed effect:
- Trainer-side comparisons could not reliably access token logprobs from chat completion responses.

Source-tree scope:
- SGLang decode handler
- frontend chat postprocessing
- unit tests covering both paths

Fix direction:
- Request logprobs from SGLang
- forward `output_token_logprobs` and `output_top_logprobs`
- map them into chat completion response fields expected by downstream comparison tooling

## 2. Missing engine routes for external weight updates

Problem:
- External rollout workers needed to support the weight-update control routes expected by the trainer-side client, but the SGLang handler base did not expose the full route set.

Observed effect:
- External weight synchronization could not complete using the existing control contract.

Source-tree scope:
- SGLang handler base route registration

Fix direction:
- Register the missing engine routes needed for weight synchronization and version tracking

## 3. Finish reason `"error"` serialized in a frontend-incompatible form

Problem:
- Backend workers could emit a bare string finish reason of `"error"`.
- The frontend expected the structured error variant, not the bare string.

Observed effect:
- Chat completion responses failed to deserialize and the frontend returned `500 Internal Server Error`.

Source-tree scope:
- common engine response normalization

Fix direction:
- Normalize bare string error finish reasons into the structured error form the frontend expects

## 4. Streamed final chunks incorrectly required usage metadata

Problem:
- The SGLang decode handler assumed streamed final chunks always included `prompt_tokens`, `completion_tokens`, and `cached_tokens`.
- Under large-load generation, some final or error chunks omitted those fields.

Observed effect:
- Worker-side `KeyError: 'prompt_tokens'`
- frontend surfaced repeated backend errors and `500` responses

Source-tree scope:
- SGLang decode handler streamed token path

Fix direction:
- Treat completion usage as optional metadata
- emit `completion_usage` only when the required usage fields are present

## Recommended issue split

File four separate issues:
1. logprobs forwarding through SGLang chat completions
2. missing engine routes for external weight updates
3. frontend-incompatible bare `"error"` finish reason
4. streamed final chunks assuming mandatory usage metadata
