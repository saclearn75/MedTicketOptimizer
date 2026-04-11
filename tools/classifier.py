import json
from openai import OpenAI

client = OpenAI()

CATEGORIES = [
    "medication_error",
    "patient_fall",
    "equipment_failure",
    "lab_diagnostic_error",
    "communication_error",
    "workflow_process_issue",
    "safety_other",
]

SEVERITIES = ["low", "medium", "high"]


def classify_ticket(ticket_text: str) -> dict:
    response = client.responses.create(
        model="gpt-5.3",
        input=[
            {
                "role": "system",
                "content": (
                    "You classify healthcare incident tickets. "
                    "Return exactly the requested JSON structure."
                ),
            },
            {
                "role": "user",
                "content": f"""
Classify the following healthcare incident ticket.

Rules:
- Choose exactly one primary_category
- Put any additional applicable categories in secondary_categories
- Do not repeat the primary category in secondary_categories
- Use only the allowed categories and severity values

Ticket:
{ticket_text}
""",
            },
        ],
        text={
            "format": {
                "type": "json_schema",
                "name": "ticket_classification",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "primary_category": {
                            "type": "string",
                            "enum": CATEGORIES,
                        },
                        "secondary_categories": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "enum": CATEGORIES,
                            },
                        },
                        "severity": {
                            "type": "string",
                            "enum": SEVERITIES,
                        },
                        "requires_escalation": {
                            "type": "boolean",
                        },
                        "brief_reason": {
                            "type": "string",
                        },
                    },
                    "required": [
                        "primary_category",
                        "secondary_categories",
                        "severity",
                        "requires_escalation",
                        "brief_reason",
                    ],
                    "additionalProperties": False,
                },
            }
        },
    )

    return json.loads(response.output_text)


if __name__ == "__main__":
    ticket = (
        "Patient attempted to walk unassisted, fell near bedside, "
        "and was later found to have received the wrong evening medication "
        "due to a charting error. Physician notified. Patient stable."
    )

    result = classify_ticket(ticket)
    print(json.dumps(result, indent=2))


