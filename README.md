# ts-fill-in-middle
Examples of how to use DeepSeek Coder LLM for Typescript Fill in Middle (FIM) tasks

### Introduction

Fine-tuned version of deepseek-ai/deepseek-coder-1.3b-base using 0.5B of TypeScript code from bigcode/the-stack-dedup. [link](https://ollama.com/codegpt/deepseek-coder-1.3b-typescript)

### Usage

This model is for completion purposes only.

```
curl http://localhost:11434/api/generate \
-d '{ "model" : "codegpt/deepseek-coder-1.3b-typescript",
      "prompt" : "class Person",
      "stream" : false,
      "options": {
	"stop" : ["\n\n"]
	}
}'
```

### Fill In the Middle (FIM)

DeepSeek models support FIM. For example,

```
<｜fim▁begin｜>function quickSort(arr: number[]): number[] {
  if (arr.length <= 1) {
    return arr;
  }
  const pivot = arr[0];
  const left = [];
  const right = [];
<｜fim▁hole｜>
  return [...quickSort(left), pivot, ...quickSort(right)];
}<｜fim▁end｜>
```

will generate

```
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < pivot) {
      left.push(arr[i]);
    } else {
      right.push(arr[i]);
    }
  }
```
