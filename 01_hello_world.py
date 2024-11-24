import sys
from openai import OpenAI
from textwrap import wrap

def main():
    openai = OpenAI()
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": "Czym jest OpenAI API?"
            }
        ]
    )
    print("\n".join(wrap(response.choices[0].message.content)))
    return 0

if __name__ == '__main__':
    sys.exit(main())
