import streamlit as st

st.set_page_config(page_title="Recursion Quest", page_icon="🔁", layout="wide")

# ---------------- STATE ----------------
def init():
    if "xp" not in st.session_state:
        st.session_state.xp = 0
    if "completed" not in st.session_state:
        st.session_state.completed = []

def award(world):
    if world not in st.session_state.completed:
        st.session_state.completed.append(world)
        st.session_state.xp += 10
        st.success(f"✅ Completed {world} (+10 XP)")
        st.balloons()

def progress():
    return len(st.session_state.completed) / 6

def build_ackermann_tree(m, n, depth=0, max_depth=4):
    """
    Builds a visual tree (as text) for Ackermann recursion.
    max_depth prevents infinite explosion.
    """
    indent = "   " * depth

    if depth > max_depth:
        return f"{indent}...\n"

    if m == 0:
        return f"{indent}A({m},{n}) → {n+1}\n"

    if n == 0:
        result = f"{indent}A({m},{n})\n"
        result += build_ackermann_tree(m-1, 1, depth+1, max_depth)
        return result

    result = f"{indent}A({m},{n})\n"
    result += build_ackermann_tree(m, n-1, depth+1, max_depth)
    result += build_ackermann_tree(m-1, 0, depth+1, max_depth)
    return result

init()

# ---------------- NAV ----------------
pages = [
    "Home",
    "World 1: What is Recursion?",
    "World 2: Recursion in the Real World",
    "World 3: Recursion Across Disciplines",
    "World 4: Core Concepts",
    "World 5: Ackermann Function",
    "World 6: Trace the Ackermann Function",
]

page = st.sidebar.radio("Navigation", pages)

st.sidebar.metric("XP", st.session_state.xp)
st.sidebar.progress(progress())

# ---------------- HOME ----------------
if page == "Home":
    st.title("🔁 Recursion Quest")
    st.write("""
    Welcome to **Recursion Quest**.

    You will:
    - Understand recursion deeply
    - See it in real life
    - Connect it across disciplines
    - Master one of the hardest recursion functions: Ackermann
    """)

# ---------------- WORLD 1 ----------------
elif page == "World 1: What is Recursion?":
    st.header("World 1: What is Recursion?")

    st.write("""
    Recursion is when a function calls itself to solve smaller versions of the same problem.
    """)

    st.code("""
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
    """)

    answer = st.radio(
        "Which best defines recursion?",
        [
            "A loop that runs forever",
            "A function that calls itself with smaller inputs",
            "A function that runs once",
            "A function that stores data"
        ]
    )

    if st.button("Check"):
        if answer == "A function that calls itself with smaller inputs":
            award("World 1")
        else:
            st.warning("Try again")

# ---------------- WORLD 2 ----------------
elif page == "World 2: Recursion in the Real World":
    st.header("World 2: Real World Recursion")

    st.write("""
    Recursion appears in:
    - Mirrors reflecting mirrors
    - Family trees
    - Nested dolls
    - Fractals
    """)

    ans = st.multiselect(
        "Select recursion examples",
        ["Family tree", "Mirror reflections", "Single object", "Nested dolls"]
    )

    if st.button("Submit"):
        if set(ans) == {"Family tree", "Mirror reflections", "Nested dolls"}:
            award("World 2")
        else:
            st.warning("Look for repeating structure")

# ---------------- WORLD 3 ----------------
elif page == "World 3: Recursion Across Disciplines":
    st.header("World 3: Interdisciplinary Recursion")

    st.markdown("""
    **Computer Science** → tree traversal, algorithms  
    **Psychology** → self-reflection loops  
    **Physics** → fractals, wave repetition  
    **Forensics** → tracing patterns recursively  
    **Engineering** → breaking systems into subsystems  
    **Cybersecurity** → recursive attack/path analysis  
    """)

    q = st.radio(
        "Which field uses recursion for breaking systems into smaller parts?",
        ["Engineering", "Driving", "Cooking", "Drawing"]
    )

    if st.button("Check"):
        if q == "Engineering":
            award("World 3")
        else:
            st.warning("Think systems decomposition")

# ---------------- WORLD 4 ----------------
elif page == "World 4: Core Concepts":
    st.header("World 4: Core Concepts")

    st.write("""
    Every recursion needs:
    1. Base case → stops recursion
    2. Recursive case → calls itself
    """)

    q = st.radio(
        "What happens if there is NO base case?",
        [
            "The program stops",
            "The recursion runs forever (stack overflow)",
            "Nothing happens",
            "It becomes a loop"
        ]
    )

    if st.button("Submit"):
        if q == "The recursion runs forever (stack overflow)":
            award("World 4")
        else:
            st.warning("Think about infinite calls")

# ---------------- WORLD 5 ----------------
elif page == "World 5: Ackermann Function":
    st.header("World 5: Ackermann Function")

    st.code("""
def A(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return A(m-1, 1)
    else:
        return A(m-1, A(m, n-1))
    """)

    st.write("""
    Why is Ackermann important?

    - Shows extreme recursion growth
    - Cannot be simplified easily
    - Used in theoretical CS
    """)

    q = st.radio(
        "What does Ackermann demonstrate?",
        [
            "Sorting",
            "Deep recursion growth",
            "Loops",
            "Storage"
        ]
    )

    if st.button("Submit"):
        if q == "Deep recursion growth":
            award("World 5")
        else:
            st.warning("Focus on recursion depth")

# ---------------- WORLD 6 ----------------
elif page == "World 6: Trace the Ackermann Function":
    st.header("🌳 World 6: Ackermann Recursion Tree")

    st.subheader("Python Function")
    st.code("""
def A(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return A(m-1, 1)
    else:
        return A(m-1, A(m, n-1))
    """)

    st.write("Now visualize recursion as a TREE instead of a list.")

    # Inputs
    col1, col2 = st.columns(2)
    with col1:
        m = st.selectbox("Select m", [0,1,2,3], index=2)
    with col2:
        n = st.selectbox("Select n", [0,1,2,3], index=2)

    st.warning("Tip: Keep values small (m ≤ 3) or the tree grows VERY fast.")

    if st.button("Generate Recursion Tree"):
        tree = build_ackermann_tree(m, n)
        st.code(tree)

    st.subheader("What you're seeing")

    st.markdown("""
    - Each line is a **function call**
    - Indentation shows **depth (call stack)**
    - Deeper = more recursive calls
    - Base case returns values back up the tree
    """)

    st.subheader("Mini Quiz")

    q = st.radio(
        "What does deeper indentation represent?",
        [
            "More loops",
            "More recursion depth (call stack)",
            "Faster execution",
            "Less memory"
        ]
    )

    if st.button("Check Concept"):
        if q == "More recursion depth (call stack)":
            st.success("Correct! Depth = stack growth")
        else:
            st.error("Think about nested function calls")

    st.subheader("Final Challenge")

    final = st.radio(
        "What is A(2,2)?",
        ["4", "5", "7", "9"]
    )

    if st.button("Submit Final"):
        if final == "7":
            st.success("🎯 Correct! A(2,2) = 7")
            award("World 6")
        else:
            st.error("Use the tree to trace carefully")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Ladelle Diekhoff - Recursion Quest, recursion trees, and student tracking")
