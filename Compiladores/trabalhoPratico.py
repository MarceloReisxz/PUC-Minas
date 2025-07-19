class MaquinaVirtual:
    def __init__(self):
        self.stack = []
        self.vars = {}
        self.labels = {}
        self.instructions = []
        self.ip = 0
        self.call_stack = []

    def load_program(self, lines):
        self.instructions = []
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            if ":" in line:
                label = line.replace(":", "").strip()
                self.labels[label] = len(self.instructions)
            else:
                self.instructions.append(line)

    def run(self):
        while self.ip < len(self.instructions):
            inst = self.instructions[self.ip].strip()
            parts = inst.split()
            op = parts[0]

            if op == "PUSH":
                self.stack.append(int(parts[1]))
            elif op == "POP":
                if self.stack:
                    self.stack.pop()
            elif op == "ADD":
                if len(self.stack) >= 2:
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(a + b)
            elif op == "SUB":
                if len(self.stack) >= 2:
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(a - b)
            elif op == "MUL":
                if len(self.stack) >= 2:
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(a * b)
            elif op == "DIV":
                if len(self.stack) >= 2:
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(a // b)
            elif op == "MOD":
                if len(self.stack) >= 2:
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(a % b)
            elif op == "NEG":
                if self.stack:
                    a = self.stack.pop()
                    self.stack.append(-a)

            elif op == "STORE":
                if self.stack:
                    val = self.stack.pop()
                    self.vars[parts[1]] = val
            elif op == "LOAD":
                self.stack.append(self.vars.get(parts[1], 0))

            elif op == "JMP":
                self.ip = self.resolve_label(parts[1])
                continue
            elif op == "JZ":
                if self.stack:
                    val = self.stack.pop()
                    if val == 0:
                        self.ip = self.resolve_label(parts[1])
                        continue
            elif op == "JNZ":
                if self.stack:
                    val = self.stack.pop()
                    if val != 0:
                        self.ip = self.resolve_label(parts[1])
                        continue
            elif op == "HALT":
                break

            elif op == "EQ":
                if len(self.stack) >= 2:
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(1 if a == b else 0)
            elif op == "NEQ":
                if len(self.stack) >= 2:
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(1 if a != b else 0)
            elif op == "LT":
                if len(self.stack) >= 2:
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(1 if a < b else 0)
            elif op == "GT":
                if len(self.stack) >= 2:
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(1 if a > b else 0)
            elif op == "LE":
                if len(self.stack) >= 2:
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(1 if a <= b else 0)
            elif op == "GE":
                if len(self.stack) >= 2:
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(1 if a >= b else 0)

            elif op == "CALL":
                self.call_stack.append(self.ip + 1)
                self.ip = self.resolve_label(parts[1])
                continue
            elif op == "RET":
                self.ip = self.call_stack.pop()
                continue

            elif op == "PRINT":
                if self.stack:
                    val = self.stack.pop()
                    print(val)
            elif op == "READ":
                val = int(input())
                self.stack.append(val)
            else:
                raise Exception(f"Instrução desconhecida: {op}")

            self.ip += 1

    def resolve_label(self, label_or_addr):
        if label_or_addr.isdigit():
            return int(label_or_addr)
        elif label_or_addr in self.labels:
            return self.labels[label_or_addr]
        else:
            raise Exception(f"Label desconhecido: {label_or_addr}")


if __name__ == "__main__":
    import sys

    lines = sys.stdin.read().splitlines()
    vm = MaquinaVirtual()
    vm.load_program(lines)
    vm.run()