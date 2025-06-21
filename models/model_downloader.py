from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="unsloth/DeepSeek-R1-0528-Qwen3-8B-GGUF",
    local_dir="models/deepseek-r1-0528",
    allow_patterns=["*Q4_K_M.gguf"]
)
