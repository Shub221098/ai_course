# Section 12: Multimodal AI

> Comprehensive, clear answers for all 30 Multimodal AI questions.

---

### Q1: What are Multimodal AI models?
**Answer:** Models capable of processing, understanding, and generating content across multiple data modalities (e.g. text, images, audio, video).

---

### Q2: How do vision-language models (VLMs) process images?
**Answer:** VLMs split images into non-overlapping spatial patches (e.g. 16x16 pixels), project patches to linear embedding vectors, and feed them alongside text tokens into Transformer layers.

---

### Q3: How do Image Embeddings work?
**Answer:** Image embedding models (like ViT) convert raw pixel matrices into dense continuous vectors representing visual concepts and spatial features.

---

### Q4: How does CLIP work, and why is it important?
**Answer:** CLIP trains an Image Encoder and Text Encoder together using contrastive loss on `(image, text)` pairs, enabling zero-shot classification and cross-modal search.

---

### Q5: Key architectures for multimodal models.
**Answer:**
- **Cross-Attention Fusion:** Text transformer attends to visual features.
- **Unified Decoder (Early Fusion):** Image patch tokens and text tokens concatenated in a single Transformer.

---

### Q6: How does image generation work with diffusion models?
**Answer:** Diffusion models start from random Gaussian noise and iteratively remove noise over multiple steps (guided by text prompt embeddings) to construct clean images.

---

### Q7: What is text-to-speech (TTS), and what models are used?
**Answer:** TTS converts text strings into audio waveforms. Modern models: VITS, Bark, ElevenLabs, XTTS.

---

### Q8: How does speech-to-text (Whisper) work?
**Answer:** Whisper uses an Encoder-Decoder Transformer: Spectrogram audio features pass through the Encoder, and the Decoder autoregressively generates text transcripts.

---

### Q9: Latency budget for real-time voice agent.
**Answer:** Target $<600\text{ ms}$ total: VAD (50ms) + ASR (100ms) + LLM TTFT (200ms) + TTS (150ms) + Network (100ms).

---

### Q10: Handling barge-in (user interruptions) in voice agents.
**Answer:** When VAD detects user speaking during TTS playback, send WebSocket interrupt signal to halt TTS generation and flush audio buffer instantly.

---

### Q11: Cascaded (ASR + LLM + TTS) vs Native Speech-to-Speech models.
**Answer:**
- **Cascaded:** Flexible, easy to debug, but higher latency & loses vocal tone/emotion.
- **Native (GPT-4o):** Sub-300ms latency, captures tone & emotion, but harder to inspect/guardrail.

---

### Q12: What is Multimodal RAG?
**Answer:** RAG retrieving both text passages and visual assets (images, diagram vectors) to answer queries requiring visual context.

---

### Q13: Building a system processing images and text.
**Answer:** Encode images into patch tokens, concatenate with text prompt tokens, and pass through a Vision-Language Model (e.g. Llama 3.2 Vision).

---

### Q14: What are multimodal embeddings?
**Answer:** Shared vector spaces where text descriptions and visual assets are mapped to identical coordinate dimensions.

---

### Q15: How to evaluate multimodal AI systems?
**Answer:** Use benchmarks like VQA v2, MathVista, MMMU, alongside LLM-as-a-judge visual evaluation rubrics.

---

### Q16: Challenges of real-time multimodal processing.
**Answer:** High GPU VRAM footprint for high-res images, processing latency, and streaming synchronization across audio/video channels.

---

### Q17: Handling video understanding with AI.
**Answer:** Extract temporal keyframes, run spatial image encoding per frame, and pass frame embeddings through temporal attention layers.

---

### Q18: What is Visual Question Answering (VQA)?
**Answer:** A multimodal task where the system answers natural language questions based on an input image.

---

### Q19: Document understanding (parsing PDFs with layouts).
**Answer:** Using vision models (ColPali / LlamaParse) that process full document page images directly, understanding tables, headers, and column reading order.

---

### Q20: How to fine-tune a vision-language model?
**Answer:** Freeze Vision Encoder, attach LoRA adapters to LLM decoder weights, and fine-tune on visual instruction pairs `(Image, Prompt, Response)`.

---

### Q21: Latency and cost considerations for multimodal AI.
**Answer:** High resolution images increase prompt token counts significantly (e.g., 1 image = 1000+ tokens), driving up latency and API costs.

---

### Q22: Multimodal content moderation.
**Answer:** Pass images through vision safety classifiers and audio through speech safety tools to catch harmful visual/vocal content.

---

### Q23: Text-to-video generation state-of-the-art.
**Answer:** Spatiotemporal Diffusion Transformers (DiT) operating on 3D latent video blocks (e.g., Sora, Runway Gen-3, Flux).

---

### Q24: Early Fusion vs Late Fusion.
**Answer:**
- **Early Fusion:** Combines raw modality tokens at the input layer.
- **Late Fusion:** Processes modalities in separate networks, merging final hidden states.

---

### Q25: VLM generates factually incorrect image descriptions. Fix?
**Answer:** Increase input image resolution, use high-capacity vision encoders, and add grounded visual system prompts.

---

### Q26: VLM answers single-image questions but fails on multi-page docs. Fix?
**Answer:** Use multi-image chunking strategies, extract text via layout-aware OCR, or use long-context VLMs.

---

### Q27: Multimodal LLM ignores image and generates descriptions from text alone. Fix?
**Answer:** Increase visual projection layer weights during fine-tuning and place image tokens *before* text tokens in prompt structure.

---

### Q28: Diffusion model ignores precise text prompt requirements. Fix?
**Answer:** Increase Classifier-Free Guidance (CFG) scale or use ControlNet / IP-Adapter conditionings.

---

### Q29: Diffusion model generates sharp but repetitive images. Fix?
**Answer:** Lower CFG scale, introduce latent noise variation, and diversify prompt text seeds.

---

### Q30: Diffusion model takes too long per image. Speed up sampling?
**Answer:** Use distilled sampler algorithms (LCM - Latent Consistency Models / SDXL Turbo) that generate images in 1-4 steps instead of 50 steps.
