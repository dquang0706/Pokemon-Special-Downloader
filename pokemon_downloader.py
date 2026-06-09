#!/usr/bin/env python3
"""
Pokemon Dac Biet Downloader
Chay: python pokemon_downloader.py
Mo trinh duyet: http://localhost:8080
"""

import http.server
import json
import threading
import urllib.request
import urllib.parse
import urllib.error
import os
import time
import socket
import ssl
from concurrent.futures import ThreadPoolExecutor

ssl._create_default_https_context = ssl._create_unverified_context

# ── Cấu hình ──────────────────────────────────────────────
PORT = 8080
BASE_URL = "https://archive.org/download/pokemon-dac-biet"
DEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")
socket.setdefaulttimeout(120)

FILES = [
    "Pokémon Đặc Biệt_Tập 01_Red Blue Green.pdf",
    "Pokémon Đặc Biệt_Tập 02_Red Blue Green.pdf",
    "Pokémon Đặc Biệt_Tập 03_Red Blue Green.pdf",
    "Pokémon Đặc Biệt_Tập 04_Yellow.pdf",
    "Pokémon Đặc Biệt_Tập 05_Yellow.pdf",
    "Pokémon Đặc Biệt_Tập 06 _Yellow.pdf",
    "Pokémon Đặc Biệt_Tập 07_Yellow.pdf",
    "Pokémon Đặc Biệt_Tập 08_Gold Silver Crystal.pdf",
    "Pokémon Đặc Biệt_Tập 09_Gold Silver Crystal.pdf",
    "Pokémon Đặc Biệt_Tập 10_ Gold Silver Crystal.pdf",
    "Pokémon Đặc Biệt_ Tập 11 Gold Siver Crystal.pdf",
    "Pokémon Đặc Biệt_ Tập 12 Gold Siver Crystal.pdf",
    "Pokémon Đặc Biệt_ Tập 13 Gold Siver Crystal.pdf",
    "Pokémon Đặc Biệt_ Tập 14 Gold Siver Crystal.pdf",
    "Pokémon Đặc Biệt_ Tập 15 Ruby Sapphire.pdf",
    "Pokémon Đặc Biệt_ Tập 16 Ruby Sapphire.pdf",
    "Pokémon Đặc Biệt_ Tập 17 Ruby Sapphire.pdf",
    "Pokémon Đặc Biệt_ Tập 18 Ruby Sapphire.pdf",
    "Pokémon Đặc Biệt_ Tập 19 Ruby Sapphire.pdf",
    "Pokémon Đặc Biệt_ Tập 20 Ruby Sapphire.pdf",
    "Pokémon Đặc Biệt_ Tập 21 Ruby Sapphire.pdf",
    "Pokémon Đặc Biệt_ Tập 22 Ruby Sapphire.pdf",
    "Pokémon Đặc Biệt_ Tập 23 Fire red Leaf green.pdf",
    "Pokémon Đặc Biệt_ Tập 24 Fire red Leaf green.pdf",
    "Pokémon Đặc Biệt_ Tập 25 Fire red Leaf green.pdf",
    "Pokémon Đặc Biệt_ Tập 26 Emerald.pdf",
    "Pokémon Đặc Biệt_ Tập 27 Emerald.pdf",
    "Pokémon Đặc Biệt_ Tập 28 Emerald.pdf",
    "Pokémon Đặc Biệt_ Tập 29 Emerald.pdf",
    "Pokémon Đặc Biệt_ Tập 30 Diamond Pearl.pdf",
    "Pokémon Đặc Biệt_ Tập 31 Diamond Pearl.pdf",
    "Pokémon Đặc Biệt_ Tập 32 Diamond Pearl.pdf",
    "Pokémon Đặc Biệt_ Tập 33 Diamond Pearl.pdf",
    "Pokémon Đặc Biệt_ Tập 34 Diamond Pearl.pdf",
    "Pokémon Đặc Biệt_ Tập 35 Diamond Pearl.pdf",
    "Pokémon Đặc Biệt_ Tập 36 Diamond Pearl.pdf",
    "Pokémon Đặc Biệt_ Tập 37 Diamond Pearl.pdf",
    "Pokémon Đặc Biệt_ Tập 38 Platinum.pdf",
    "Pokémon Đặc Biệt_ Tập 39 Platinum.pdf",
    "Pokémon Đặc Biệt_ Tập 40 Platinum.pdf",
    "Pokémon Đặc Biệt_ Tập 41 Heart Gold Soul Silver.pdf",
    "Pokémon Đặc Biệt_ Tập 42 Heart Gold Soul Silver.pdf",
    "Pokémon Đặc Biệt_ Tập 43 Black White.pdf",
    "Pokémon Đặc Biệt_ Tập 44 Black White.pdf",
    "Pokémon Đặc Biệt_ Tập 45 Black White.pdf",
    "Pokémon Đặc Biệt_ Tập 46 Black White.pdf",
    "Pokémon Đặc Biệt_ Tập 47 Black White.pdf",
    "Pokémon Đặc Biệt_ Tập 48 Black White.pdf",
    "Pokémon Đặc Biệt_ Tập 49 Black White.pdf",
    "Pokémon Đặc Biệt_ Tập 50 Black White.pdf",
    "Pokémon Đặc Biệt_ Tập 51 Black White.pdf",
    "Pokémon Đặc Biệt_ Tập 52 Black2 White2.pdf",
    "Pokémon Đặc Biệt_ Tập 53 Black2 White2.pdf",
    "Pokémon Đặc Biệt_ Tập 54 Black2 White2.pdf",
    "Pokémon Đặc Biệt_ Tập 55 XY.pdf",
    "Pokémon Đặc Biệt_ Tập 56 XY.pdf",
    "Pokémon Đặc Biệt_ Tập 57 XY.pdf",
    "Pokémon Đặc Biệt_ Tập 58 XY.pdf",
    "Pokémon Đặc Biệt_ Tập 59 XY.pdf",
    "Pokémon Đặc Biệt_ Tập 60 XY.pdf",
    "Pokémon Đặc Biệt_ Tập 61 XY.pdf",
    "Pokémon Đặc Biệt_ Tập 62 Omega Ruby Alpha Sapphire.pdf",
    "Pokémon Đặc Biệt_ Tập 63 Omega Ruby Alpha Sapphire.pdf",
    "Pokémon Đặc Biệt_ Tập 64 Omega Ruby Alpha Sapphire.pdf",
    "Pokémon Đặc Biệt_ Tập 65 Sun Moon.pdf",
    "Pokémon Đặc Biệt_ Tập 66 Sun Moon.pdf",
    "Pokémon Đặc Biệt_ Tập 67 Sun Moon.pdf",
    "Pokémon Đặc Biệt_ Tập 68 Sun Moon.pdf",
    "Pokémon Đặc Biệt_ Tập 69 Sun Moon.pdf",
    "Pokémon Đặc Biệt_ Tập 70 Sun Moon.pdf",
    "Pokémon Đặc Biệt_ Tập 71 Sworld Shield.pdf",
    "Pokémon Đặc Biệt_ Tập 72 Sworld Shield.pdf",
    "Pokémon Đặc Biệt_ Tập 73 Sworld Shield.pdf",
    "Pokémon Đặc Biệt_ Tập 74 Sworld Shield.pdf",
    "Pokémon Đặc Biệt_ Tập 75 Sworld Shield.pdf",
    "Pokémon Đặc Biệt_ Tập 76 Sworld Shield.pdf",
    "Pokémon Đặc Biệt_ Tập 77 Sworld Shield.pdf",
    "Pokémon Đặc Biệt_ Tập 78 Scarlet Violet.pdf",
    "Pokémon Đặc Biệt_ Tập 79 Scarlet Violet.pdf",
    "Pokémon Đặc Biệt_ Tập 80 Scarlet Violet.pdf",
    "Pokémon Đặc Biệt_ Tập 81 Scarlet Violet.pdf",
]

# ── State ──────────────────────────────────────────────────
_lock = threading.Lock()
_state = {"running": False, "done": 0, "skip": 0, "fail": 0}
_logs = []
_stop = threading.Event()


def add_log(msg):
    ts = time.strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    with _lock:
        _logs.append(line)
        if len(_logs) > 1000:
            del _logs[:200]
    print(line)


def download_file(filename):
    print(f"[DEBUG] download_file called for: {filename}")
    if _stop.is_set():
        return

    dest = os.path.join(DEST, filename)
    if os.path.isfile(dest):
        add_log(f"⏭ BỎ QUA: {filename}")
        with _lock:
            _state["skip"] += 1
        return

    url = BASE_URL + "/" + urllib.parse.quote(filename)
    tmp = dest + ".tmp"

    add_log(f"⬇ BẮT ĐẦU: {filename}")
    add_log(f"🔗 URL: {url}")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp, open(tmp, "wb") as f:
            while True:
                if _stop.is_set():
                    break
                chunk = resp.read(65536)
                if not chunk:
                    break
                f.write(chunk)

        if _stop.is_set():
            if os.path.exists(tmp):
                os.remove(tmp)
            return

        os.rename(tmp, dest)
        add_log(f"✅ XONG: {filename}")
        with _lock:
            _state["done"] += 1

    except Exception as e:
        import traceback
        add_log(f"❌ LỖI: {filename} — {e}")
        add_log(f"🔴 TRACE: {traceback.format_exc()}")
        if os.path.exists(tmp):
            os.remove(tmp)
        with _lock:
            _state["fail"] += 1


def run_downloads(parallel):
    os.makedirs(DEST, exist_ok=True)
    _stop.clear()
    with _lock:
        _state.update({"running": True, "done": 0, "skip": 0, "fail": 0})
        _logs.clear()

    add_log(f"🚀 Bắt đầu tải {len(FILES)} tập | {parallel} luồng song song")
    add_log(f"📁 Lưu vào: {DEST}")

    with ThreadPoolExecutor(max_workers=parallel) as ex:
        list(ex.map(download_file, FILES))

    with _lock:
        _state["running"] = False
        d, s, f = _state["done"], _state["skip"], _state["fail"]

    add_log(f"🏁 Hoàn thành! ✅ {d} xong | ⏭ {s} bỏ qua | ❌ {f} lỗi")


# ── HTML ───────────────────────────────────────────────────
HTML = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Pokemon Dac Biet Downloader</title>
<style>
  *{margin:0;padding:0;box-sizing:border-box}
  body{font-family:'Courier New',monospace;background:#0d1117;color:#c9d1d9;min-height:100vh;padding:24px}
  h1{color:#f0c040;font-size:1.4rem;margin-bottom:4px}
  .sub{color:#8b949e;font-size:.8rem;margin-bottom:24px}
  .stats{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:16px}
  .stat{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:12px 20px;text-align:center;min-width:90px}
  .stat-val{font-size:1.8rem;font-weight:bold}
  .stat-lbl{font-size:.7rem;color:#8b949e;margin-top:2px}
  .total .stat-val{color:#58a6ff}
  .done  .stat-val{color:#3fb950}
  .skip  .stat-val{color:#d29922}
  .fail  .stat-val{color:#f85149}
  .bar{background:#21262d;border-radius:6px;height:8px;margin-bottom:18px;overflow:hidden}
  .fill{height:100%;background:linear-gradient(90deg,#1f6feb,#3fb950);transition:width .4s;border-radius:6px}
  .controls{display:flex;gap:10px;align-items:center;margin-bottom:16px;flex-wrap:wrap}
  button{padding:9px 22px;border:none;border-radius:6px;font-size:.85rem;cursor:pointer;font-family:inherit;transition:opacity .2s}
  button:hover{opacity:.82}
  button:disabled{opacity:.3;cursor:not-allowed}
  #btn-start{background:#238636;color:#fff}
  #btn-stop{background:#da3633;color:#fff}
  .lbl{color:#8b949e;font-size:.8rem}
  input[type=number]{background:#21262d;border:1px solid #30363d;color:#c9d1d9;padding:8px 10px;border-radius:6px;width:56px;font-size:.85rem;font-family:inherit}
  .dest-box{background:#21262d;border:1px solid #30363d;border-radius:6px;padding:8px 12px;font-size:.78rem;color:#8b949e;margin-bottom:16px;word-break:break-all}
  .log-wrap{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:14px;height:420px;overflow-y:auto;font-size:.78rem;line-height:1.65}
  .line{white-space:pre-wrap;word-break:break-all}
  .line.ok{color:#3fb950}
  .line.sk{color:#d29922}
  .line.er{color:#f85149}
  .line.dl{color:#58a6ff}
  .line.in{color:#c9d1d9}
</style>
</head>
<body>
<h1>&#128994; Pokemon Dac Biet Downloader</h1>
<p class="sub">Nguon: archive.org/download/pokemon-dac-biet &nbsp;|&nbsp; 81 tap</p>

<div class="stats">
  <div class="stat total"><div class="stat-val" id="s-total">81</div><div class="stat-lbl">Tong</div></div>
  <div class="stat done"> <div class="stat-val" id="s-done">0</div> <div class="stat-lbl">Xong</div></div>
  <div class="stat skip"> <div class="stat-val" id="s-skip">0</div> <div class="stat-lbl">Bo qua</div></div>
  <div class="stat fail"> <div class="stat-val" id="s-fail">0</div> <div class="stat-lbl">Loi</div></div>
</div>

<div class="bar"><div class="fill" id="bar" style="width:0%"></div></div>

<div class="controls">
  <button id="btn-start" onclick="doStart()">&#9654; Bat dau tai</button>
  <button id="btn-stop"  onclick="doStop()" disabled>&#9632; Dung lai</button>
  <span class="lbl">Luong song song:</span>
  <input id="p-in" type="number" value="4" min="1" max="10">
</div>

<div class="dest-box">&#128193; Thu muc luu: <span id="dest-path">...</span></div>

<div class="log-wrap" id="log"></div>

<script>
function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
function cls(l){
  if(/XONG|✅/.test(l)) return 'ok';
  if(/BỎ QUA|⏭/.test(l)) return 'sk';
  if(/LỖI|❌/.test(l))  return 'er';
  if(/BẮT ĐẦU|⬇/.test(l)) return 'dl';
  return 'in';
}
let lastLen=0;
async function poll(){
  try{
    const d=await(await fetch('/status')).json();
    document.getElementById('s-total').textContent=d.total;
    document.getElementById('s-done').textContent=d.done;
    document.getElementById('s-skip').textContent=d.skip;
    document.getElementById('s-fail').textContent=d.fail;
    document.getElementById('dest-path').textContent=d.dest;
    const fin=d.done+d.skip+d.fail;
    document.getElementById('bar').style.width=(fin/d.total*100)+'%';
    if(d.logs.length!==lastLen){
      lastLen=d.logs.length;
      const box=document.getElementById('log');
      const atBot=box.scrollHeight-box.scrollTop<=box.clientHeight+60;
      box.innerHTML=d.logs.map(l=>`<div class="line ${cls(l)}">${esc(l)}</div>`).join('');
      if(atBot) box.scrollTop=box.scrollHeight;
    }
    if(!d.running){
      document.getElementById('btn-start').disabled=false;
      document.getElementById('btn-stop').disabled=true;
    }
  }catch(e){}
}
async function doStart(){
  const p=parseInt(document.getElementById('p-in').value)||4;
  await fetch('/start?p='+p,{method:'POST'});
  document.getElementById('btn-start').disabled=true;
  document.getElementById('btn-stop').disabled=false;
  poll();
}
async function doStop(){
  await fetch('/stop',{method:'POST'});
  document.getElementById('btn-stop').disabled=true;
}
poll();
setInterval(poll,2000);
</script>
</body>
</html>"""


# ── HTTP Handler ───────────────────────────────────────────
class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            body = HTML.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        elif self.path == "/status":
            with _lock:
                data = dict(_state)
            data["total"] = len(FILES)
            data["dest"] = DEST
            data["logs"] = list(_logs[-200:])
            body = json.dumps(data, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path.startswith("/start"):
            with _lock:
                running = _state["running"]
            if not running:
                qs = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
                parallel = int(qs.get("p", ["4"])[0])
                parallel = max(1, min(parallel, 16))
                t = threading.Thread(target=run_downloads, args=(parallel,), daemon=True)
                t.start()
            self._json({"ok": True})

        elif self.path == "/stop":
            _stop.set()
            with _lock:
                _state["running"] = False
            add_log("🛑 Đã dừng bởi người dùng")
            self._json({"ok": True})

        else:
            self.send_response(404)
            self.end_headers()

    def _json(self, data):
        body = json.dumps(data).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass  # tắt request log


# ── Main ───────────────────────────────────────────────────
if __name__ == "__main__":
    os.makedirs(DEST, exist_ok=True)
    print(f"Pokemon Dac Biet Downloader")
    print(f"Mo trinh duyet: http://localhost:{PORT}")
    print(f"Thu muc luu   : {DEST}")
    print("Nhan Ctrl+C de dung server\n")
    server = http.server.HTTPServer(("", PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDa dung server.")
