<div align="center">

<img src="docs/images/logo-banner.gif" alt="SonicFlow AI — stream voice with ultra-low latency" width="920"/>

# SonicFlow AI

### *Next-Generation Real-Time Voice Agent Platform*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-green.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-latest-teal.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-ready-blue.svg)](https://www.docker.com/)

**Built with ❤️ by Keshav**

[Features](#-key-features) • [Architecture](#-system-architecture) • [Installation](#-quick-start) • [Performance](#-performance-metrics) • [Documentation](#-documentation)

---

</div>

## 🌟 Overview

**SonicFlow AI** is a cutting-edge, full-duplex streaming voice agent platform that delivers natural, low-latency conversational AI experiences. Built on state-of-the-art ML models and optimized for production deployment, it combines advanced ASR, intelligent turn-taking, sophisticated LLM conversation handling, and high-quality TTS into a seamless real-time voice interface.

### 🎯 What Makes SonicFlow Unique

- **Ultra-Low Latency**: Sub-800ms response times from speech end to audio playback
- **Natural Turn-Taking**: ML-powered interruption handling and conversation flow
- **Tool Integration**: Seamless function calling with natural language bridges
- **Production Ready**: Auto-scaling GPU compute with scale-to-zero cost optimization
- **Research-Backed**: End-to-end reproducible ML pipeline from data generation to deployment

---

## 🚀 Key Features

### 🎤 **Advanced Speech Processing**
- Real-time streaming ASR with Nemotron encoder
- Causal turn-taking detection using custom GRU adapter
- Voice Activity Detection (VAD) with Silero
- Sub-second endpoint detection

### 🧠 **Intelligent Conversation**
- Qwen3-4B instruction-tuned language model
- Context-aware response generation
- Structured tool calling with natural bridges
- Search summarization and information retrieval

### 🔊 **Premium Text-to-Speech**
- Kyutai streaming TTS for natural voice synthesis
- Low-latency audio streaming
- Speculative generation for faster responses
- Browser-optimized audio playback

### ⚡ **Production Infrastructure**
- Modal GPU compute with auto-scaling
- Persistent model caching
- WebSocket-based streaming protocol
- Scale-to-zero cost optimization
- Cold-start optimization (<60s)

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Browser Client                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Microphone  │→→│  WebSocket   │←←│ Audio Player │          │
│  │   Capture    │  │  Connection  │  │   & Queue    │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└────────────────────────────┬────────────────────────────────────┘
                             │ 16kHz PCM + Metadata
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│                 Modal GPU Compute Layer                          │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                       GPU 0                                │  │
│  │  ┌──────────────────────────────────────────────────────┐ │  │
│  │  │  Nemotron Streaming ASR                              │ │  │
│  │  │    • Encoder feature extraction                      │ │  │
│  │  │    • Real-time transcription                         │ │  │
│  │  └──────────────┬───────────────────────────────────────┘ │  │
│  │                 │                                          │  │
│  │                 ↓                                          │  │
│  │  ┌──────────────────────────────────────────────────────┐ │  │
│  │  │  Turn-Taking Adapter (GRU)                           │ │  │
│  │  │    • Causal turn detection                           │ │  │
│  │  │    • Interruption handling                           │ │  │
│  │  │    • HOLD/EOT classification                         │ │  │
│  │  └──────────────┬───────────────────────────────────────┘ │  │
│  │                 │                                          │  │
│  │                 ↓                                          │  │
│  │  ┌──────────────────────────────────────────────────────┐ │  │
│  │  │  Qwen3-4B Conversation Engine                        │ │  │
│  │  │    • Context management                              │ │  │
│  │  │    • Tool call generation                            │ │  │
│  │  │    • Natural response synthesis                      │ │  │
│  │  └──────────────────────────────────────────────────────┘ │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                       GPU 1                                │  │
│  │  ┌──────────────────────────────────────────────────────┐ │  │
│  │  │  Kyutai Streaming TTS                                │ │  │
│  │  │    • Real-time speech synthesis                      │ │  │
│  │  │    • Audio chunk streaming                           │ │  │
│  │  └──────────────────────────────────────────────────────┘ │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │           Orchestration Layer                              │  │
│  │  • Prediction pipeline  • Tool execution                  │  │
│  │  • Cancellation logic   • Playback barriers               │  │
│  └───────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │ Streaming Audio
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│                   Persistent Storage                             │
│  • Model Cache (Modal Volume)  • Session Telemetry              │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Performance Metrics

### Response Latency Analysis

Based on real-world microphone sessions (n=36 measured turns):

| Metric | Median | Mean | Range |
|--------|--------|------|-------|
| **Final VAD → First Audio** | 758ms | 932ms | 528–1,652ms |
| **Turns under 800ms** | 58% | - | 21/36 |
| **Endpoint Decision** | 502ms | - | - |
| **LLM First Word** | 336ms | - | - |
| **TTS First PCM** | 444ms | - | - |
| **Network + Browser Render** | 95ms | - | - |

### Model Performance

**Turn Detection Accuracy**:
- HOLD false cutoff rate: 2.7% (1/37)
- EOT detection recall: 205/1,636 (12.5% threshold crossing)
- Hybrid policy provides robust fallback

**Tool Use Enhancement** (1.7B LoRA adapter on synthetic data):
- Correct tool decision: **95.2%** (vs 80.0% base)
- Exact tool name: **94.3%** (vs 78.6% base)
- Concise spoken bridge: **94.3%** (vs 7.6% base)
- Avoided unnecessary tools: **100%** (vs 70.0% base)

---

## 🛠️ Quick Start

### Prerequisites

- Python 3.11+
- Docker & Docker Compose
- PostgreSQL (optional, for analytics)
- Modal account (for cloud deployment)

### Local Development Setup

```bash
# Clone the repository
git clone https://github.com/keshav/sonicflow-ai.git
cd sonicflow-ai

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .

# Start local services
docker-compose up -d

# Run the development server
uvicorn app.main:app --reload --port 8000
```

Access the local voice agent at `http://127.0.0.1:8000/voice-agent`

### Docker Deployment

```bash
# Build the container
docker build -t sonicflow-ai:latest .

# Run with Docker Compose
docker-compose up -d

# Check health
curl http://localhost:8000/health
```

---

## 📂 Project Structure

```
sonicflow-ai/
├── app/
│   ├── main.py                 # FastAPI application entry
│   ├── voice_agent/            # Voice agent core logic
│   ├── streaming/              # WebSocket streaming handlers
│   └── tools/                  # Tool implementations
├── deployment/
│   ├── modal_app.py            # Modal deployment config
│   ├── docker/                 # Docker configurations
│   └── kubernetes/             # K8s manifests
├── synthetic-generation/
│   ├── generate_tool_use_data.py
│   ├── generate_turn_data.py
│   └── templates/              # Conversation templates
├── training/
│   ├── train_tool_use_lora.py
│   ├── train_turn_taking.py
│   └── configs/                # Training configurations
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docs/
│   ├── deployment.md
│   ├── training.md
│   └── api.md
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
└── README.md
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Application
APP_ENV=development
LOG_LEVEL=INFO

# Models
ASR_MODEL=nemotron-streaming
LLM_MODEL=qwen3-4b-instruct
TTS_MODEL=kyutai-streaming
TURN_ADAPTER_PATH=./checkpoints/turn_adapter.pt

# Modal (for cloud deployment)
MODAL_TOKEN_ID=your_token_id
MODAL_TOKEN_SECRET=your_token_secret

# Database (optional)
DATABASE_URL=postgresql://user:pass@localhost:5432/sonicflow
```

---

## 🧪 Testing

```bash
# Unit tests
pytest tests/unit -v

# Integration tests
pytest tests/integration -v

# End-to-end tests
pytest tests/e2e -v
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

**Keshav** - Project Creator & Maintainer

For questions or collaboration opportunities, feel free to reach out!

---

<div align="center">

**⭐ Star this project if you find it useful! ⭐**

Made with 💜 by Keshav

</div>
