// Post the Meme, Win the Feed — make.fun entrypoint (Node 22, standard library only).
// The entry itself is the meme post on X; this program only delivers POST.json
// to the gate by copying it from the bot directory into the output directory.
// It does not score, edit, or say anything about the post.

import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const postSource = join(botDir, "POST.json");
const postTarget = join(outDir, "POST.json");

mkdirSync(outDir, { recursive: true });

try {
  copyFileSync(postSource, postTarget);
  const post = JSON.parse(readFileSync(postTarget, "utf8"));
  if (typeof post.url !== "string" || !post.url.startsWith("https://x.com/")) {
    throw new Error(`POST.json has no valid post URL: ${postTarget}`);
  }
} catch (error) {
  const reason = error instanceof Error ? error.message : String(error);
  console.error(`could not copy POST.json from ${postSource}: ${reason}`);
  process.exit(1);
}
