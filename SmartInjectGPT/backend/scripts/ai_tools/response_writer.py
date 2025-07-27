import sys

output_path = "E:/SmartBiz_Assistance/SmartInjectGPT/scripts/generated_code.txt"

if len(sys.argv) < 2:
    print("⚠️  Usage: python response_writer.py 'your response text here'")
    sys.exit(1)

text = sys.argv[1]

with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"✅ Response written to {output_path}")
