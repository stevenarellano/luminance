import json

example1 = [
    {
        "title": "Foundations of Mathematics",
        "topics": [
            "Set theory, including the axioms of Zermelo-Fraenkel set theory and the concept of cardinality",
            "Logic, including propositional and predicate calculus, and the completeness and compactness theorems",
            "Number theory, including the fundamental theorem of arithmetic, modular arithmetic, and Diophantine equations",
            "Analysis, including limits, continuity, derivatives, and integrals"
        ]
    },
    {
        "title": "Pure Mathematics",
        "topics": [
            "Algebra, including groups, rings, and fields, and Galois theory",
            "Topology, including metric spaces, topological spaces, and homotopy theory",
            "Geometry, including Euclidean geometry, non-Euclidean geometry, and differential geometry",
            "Combinatorics, including graph theory, combinatorial designs, and Ramsey theory"
        ]
    },
    {
        "title": "Applied Mathematics",
        "topics": [
            "Differential equations, including ordinary differential equations and partial differential equations",
            "Numerical analysis, including numerical methods for solving differential equations, linear algebra, and optimization problems",
            "Probability and statistics, including stochastic processes, measure theory, and Bayesian inference",
            "Mathematical physics, including classical mechanics, quantum mechanics, and special and general relativity"
        ]
    },
    {
        "title": "Specialized Topics",
        "topics": [
            "Algebraic geometry, including the geometry of algebraic varieties, and sheaf theory",
            "Algebraic topology, including homology theory, cohomology theory, and homotopy theory",
            "Representation theory, including the theory of Lie groups, Lie algebras, and their representations",
            "Number theory, including elliptic curves, modular forms, and the Langlands program"
        ]
    }
]

example2 = [
    {
        "title": "Foundations of Computer Science",
        "topics": [
            "Boolean logic and digital circuits",
            "Data structures and algorithms",
            "Formal languages and automata theory",
            "Computability and complexity theory"
        ]
    },
    {
        "title": "Programming Languages and Compilation",
        "topics": [
            "Programming language semantics and design",
            "Compiler design and optimization",
            "Interpretation and virtual machines",
            "Type theory and type systems"
        ]
    },
    {
        "title": "Operating Systems and Computer Architecture",
        "topics": [
            "Operating system design and implementation",
            "Computer organization and architecture",
            "Distributed systems and parallel computing",
            "Memory management and file systems"
        ]
    },
    {
        "title": "Computer Networks and Security",
        "topics": [
            "Network protocols and architectures",
            "Wireless and mobile networks",
            "Network security and cryptography",
            "Cybersecurity and privacy"
        ]
    },
    {
        "title": "Artificial Intelligence and Machine Learning",
        "topics": [
            "Artificial intelligence and expert systems",
            "Machine learning and deep learning",
            "Natural language processing and speech recognition",
            "Computer vision and image processing"
        ]
    },
    {
        "title": "Databases and Information Retrieval",
        "topics": [
            "Database design and implementation",
            "Transaction processing and concurrency control",
            "Data mining and machine learning for data analysis",
            "Information retrieval and web search"
        ]
    },
    {
        "title": "Human-Computer Interaction and Graphics",
        "topics": [
            "User interface design and usability engineering",
            "Human-computer interaction and cognitive psychology",
            "Computer graphics and visualization",
            "Virtual and augmented reality"
        ]
    },
    {
        "title": "Software Engineering and Formal Methods",
        "topics": [
            "Software engineering principles and methodologies",
            "Requirements engineering and software design",
            "Software testing and quality assurance",
            "Formal methods and program verification"
        ]
    }
]


example_dict = [
    {"input": "math", "output": json.dumps(example1)},
    {"input": "computer science", "output": json.dumps(example2)}
]


print(example_dict)
