# Import necessary packages (Make sure to also include in "requirements.txt" in this repository.)
import streamlit as st
import pandas as pd

# Print Title for the App
st.title("Microsoft Stock Data Dashboard by Justin Wang")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository) 
df = pd.read_csv("msft.csv")

# Set up the tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart", "💡 Quote of the Day", "Draw"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for MSFT")
    st.dataframe(df, use_container_width=True)

# Tab 2: Closing Price Chart
with tabs[1]:
    st.subheader(f"Closing Price for MSFT")
    st.line_chart(df['Close'])

# Tab 3: Volume Chart
with tabs[2]:
    st.subheader(f"Volume for MSFT")
    st.bar_chart(df['Volume'])

#Tab 4: Quote of the Day
with tabs[3]:
    st.subheader("💡 Quote of the Day")

    from datetime import date

    quotes = [
        "The best way to predict the future is to create it.",
        "Success is not final, failure is not fatal.",
        "Dream big and dare to fail.",
        "Great things take time.",
        "Work hard in silence, let success make the noise.",
        "Every day is a new opportunity.",
        "Don't watch the clock; do what it does. Keep going."
    ]

    # Choose a different quote each day
    today = date.today()
    quote = quotes[today.toordinal() % len(quotes)]

    st.info(quote)
    st.write(f"📅 {today.strftime('%B %d, %Y')}")
    st.caption("Made by Justin Wang 🚀")


# Tab 4: Interactive Drawing Board
with tabs[4]:
    st.subheader("🎨 Justin's Drawing Board")
    st.write("Choose a shape and drag your mouse to draw!")

    import streamlit.components.v1 as components

    components.html("""
    <style>
        body { font-family: Arial, sans-serif; }
        .toolbar {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 12px;
        }
        button, select, input {
            padding: 8px;
            border-radius: 6px;
            cursor: pointer;
        }
        canvas {
            width: 100%;
            border: 2px solid #555;
            border-radius: 8px;
            background: white;
            touch-action: none;
            box-sizing: border-box;
        }
    </style>

    <div class="toolbar">
        <select id="shape">
            <option value="pen">✏️ Free Draw</option>
            <option value="rect">⬛ Rectangle</option>
            <option value="circle">⭕ Circle</option>
            <option value="triangle">🔺 Triangle</option>
            <option value="line">📏 Line</option>
        </select>

        <input type="color" id="color" value="#2563eb">
        <button id="undo">↩️ Undo</button>
        <button id="clear">🗑️ Clear</button>
    </div>

    <canvas id="board" width="850" height="400"></canvas>
    <p>Made by Justin Wang 🚀</p>

    <script>
        const canvas = document.getElementById("board");
        const ctx = canvas.getContext("2d");
        const shape = document.getElementById("shape");
        const color = document.getElementById("color");

        let shapes = [];
        let current = null;
        let drawing = false;

        function position(e) {
            const r = canvas.getBoundingClientRect();
            return {
                x: (e.clientX - r.left) * canvas.width / r.width,
                y: (e.clientY - r.top) * canvas.height / r.height
            };
        }

        function draw(s) {
            ctx.beginPath();
            ctx.strokeStyle = s.color;
            ctx.lineWidth = 4;
            ctx.lineCap = "round";
            ctx.lineJoin = "round";

            const a = s.start;
            const b = s.end;

            if (s.type === "pen") {
                s.points.forEach((p, i) => {
                    if (i === 0) ctx.moveTo(p.x, p.y);
                    else ctx.lineTo(p.x, p.y);
                });
            } else if (s.type === "rect") {
                ctx.rect(a.x, a.y, b.x - a.x, b.y - a.y);
            } else if (s.type === "circle") {
                const radius = Math.hypot(b.x - a.x, b.y - a.y);
                ctx.arc(a.x, a.y, radius, 0, Math.PI * 2);
            } else if (s.type === "line") {
                ctx.moveTo(a.x, a.y);
                ctx.lineTo(b.x, b.y);
            } else if (s.type === "triangle") {
                const left = Math.min(a.x, b.x);
                const right = Math.max(a.x, b.x);
                const top = Math.min(a.y, b.y);
                const bottom = Math.max(a.y, b.y);
                ctx.moveTo((left + right) / 2, top);
                ctx.lineTo(left, bottom);
                ctx.lineTo(right, bottom);
                ctx.closePath();
            }

            ctx.stroke();
        }

        function redraw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            shapes.forEach(draw);
            if (current) draw(current);
        }

        canvas.addEventListener("pointerdown", e => {
            drawing = true;
            const p = position(e);
            current = {
                type: shape.value,
                color: color.value,
                start: p,
                end: p,
                points: [p]
            };
            canvas.setPointerCapture(e.pointerId);
        });

        canvas.addEventListener("pointermove", e => {
            if (!drawing) return;
            const p = position(e);
            current.end = p;
            if (current.type === "pen") current.points.push(p);
            redraw();
        });

        canvas.addEventListener("pointerup", e => {
            if (!drawing) return;
            const p = position(e);
            current.end = p;
            if (current.type === "pen") current.points.push(p);
            shapes.push(current);
            current = null;
            drawing = false;
            redraw();
        });

        document.getElementById("undo").onclick = () => {
            shapes.pop();
            redraw();
        };

        document.getElementById("clear").onclick = () => {
            shapes = [];
            redraw();
        };
    </script>
    """, height=530)

    
