import { faBrain, faPhone, faPlus } from "@fortawesome/free-solid-svg-icons";
import {
  quality,
  mobile,
  calander,
  maths,
  ppt,
  assistant,
  quiz,
  book,
  speech,
  generator,
  the,
  people,
  mobilePhone,
  conversation,
  fast,
  keyboard,
  specific,
} from "../assets";
import { people01, people02, people03 } from "../assets";
import { instagram, facebook, twitter, linkedin } from "../assets";

export const quizSampleQuestions = [
  {
    index: 0,
    question: "What does CSS stand for?",
    answers: [
      { id: 0, option: "A. Cascading Style Sheets", correct: true },
      { id: 1, option: "B. Central Style System", correct: false },
      { id: 2, option: "C. Computer System Styles", correct: false },
    ],
  },
  {
    index: 1,
    question: "Which programming language is used to build Android apps?",
    answers: [
      { id: 0, option: "A. Swift", correct: false },
      { id: 1, option: "B. Java", correct: true },
      { id: 2, option: "C. Python", correct: false },
    ],
  },
  {
    index: 2,
    question: "What does HTML stand for?",
    answers: [
      { id: 0, option: "A. Hyper Text Markup Language", correct: true },
      { id: 1, option: "B. High Technology Markup Language", correct: false },
      { id: 2, option: "C. Hybrid Text Markup Language", correct: false },
    ],
  },
  {
    index: 3,
    question: "What is the difference between margin and padding in CSS?",
    answers: [
      { id: 0, option: "A. There is no difference", correct: false },
      {
        id: 1,
        option: "B. Margin is outside the border, padding is inside the border",
        correct: true,
      },
      {
        id: 2,
        option: "C. Padding is outside the border, margin is inside the border",
        correct: false,
      },
    ],
  },
  {
    index: 4,
    question: "What is an array in programming?",
    answers: [
      { id: 0, option: "A. A type of loop", correct: false },
      {
        id: 1,
        option: "B. A collection of elements of the same type",
        correct: true,
      },
      { id: 2, option: "C. A type of function", correct: false },
    ],
  },
];

export const navLinks = [
  {
    id: "home",
    title: "Home",
  },
  {
    id: "features",
    title: "Features",
  },
  {
    id: "product",
    title: "Product",
  },
  {
    id: "clients",
    title: "Clients",
  },
];

export const subjects = [
  {
    id: 1,
    title: "Maths",
    icon: maths,
  },
  {
    id: 21,
    title: "Maths",
    icon: maths,
  },
  {
    id: 3,
    title: "Maths",
    icon: maths,
  },
  {
    id: 4,
    title: "Maths",
    icon: maths,
  },
  {
    id: 5,
    title: "Maths",
    icon: maths,
  },
  {
    id: 6,
    title: "Maths",
    icon: maths,
  },
];

export const feedback = [
  {
    id: "feedback-1",
    content:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nec turpis dapibus, lacinia dui eget, elementum ex. Integer et eros ut purus hendrerit dignissim sed sed enim. Aenean lacinia purus tortor,",
    name: "Herman Jensen",
    title: "Founder & Leader",
    img: people01,
  },
  {
    id: "feedback-2",
    content:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nec turpis dapibus, lacinia dui eget, elementum ex",
    name: "Steve Mark",
    title: "Founder & Leader",
    img: people02,
  },
  {
    id: "feedback-3",
    content:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nec turpis dapibus, lacinia dui eget, elementum ex. Integer et eros ut purus hendrerit dignissim sed sed.",
    name: "Kenn Gallagher",
    title: "Founder & Leader",
    img: people03,
  },
];

export const choices = [
  {
    id: 211,
    title: `Solve all your subject problems with text and symbol containing images using over 100 languages. `,
    icon: mobile,
    path: "/text-image",
    modalDescription: "This is my modal descriptor",
    modalTitle: "OCR Feature",
  },
  {
    id: 3,
    title: `Say goodbye to clunky PowerPoint creation - use only your keyboard to make beautiful slides.`,
    icon: ppt,
    path: "/dashboard",
    modalDescription: "This is my modal descriptor",
    modalTitle: "PPT",
  },

  {
    id: 4,
    title: `Prepare fully in any type of exam with the Student.AI's Preparation system`,
    icon: quiz,
    path: "/dashboard/exam",
    modalDescription: "This is my modal descriptor",
    modalTitle: "PPT",
  },
  {
    id: 5,
    title: `Boost your writing skills with AI-powered academic writing assistance and essay writer for expert feedback and flawless compositions.`,
    icon: assistant,
    path: "/dashboard/essay",
    modalDescription: "This is my modal descriptor",
    modalTitle: "PPT",
  },
  {
    id: 6,
    title: `Streamline your reading with our automated summarization tool, turning lengthy texts into concise and clear summaries.`,
    icon: book,
    path: "/dashboard",
    modalDescription: "This is my modal descriptor",
    modalTitle: "PPT",
  },

  {
    id: 8,
    title: `Automatically generate citations for your research papers in various citation styles, saving you time and ensuring accuracy`,
    icon: generator,
    path: "/dashboard",
    modalDescription: "This is my modal descriptor",
    modalTitle: "PPT",
  },
];

export const samples = {
  slides: [
    {
      title: "Introduction to Programming",
      theme: "summer",
      imagePath: "",
      imageWidth: 0,
      imageHeight: 0,
      description:
        "Programming is the process of designing, writing, testing, and maintaining the source code of computer software. It involves using a programming language to instruct a computer to perform certain tasks. Programming has become an essential skill in today's world, with a growing demand for programmers in various industries.",
    },
    {
      title: "Programming Languages",
      theme: "programming",
      imagePath: "",
      imageWidth: 0,
      imageHeight: 0,
      description:
        "There are numerous programming languages, each with its own syntax and purpose. Some popular programming languages include: \n\n- Java: used for building desktop and web applications \n- Python: used for data analysis, machine learning, and web development \n- JavaScript: used for building dynamic web applications \n- C#: used for developing Windows desktop and mobile applications \n- Ruby: used for web development and scripting \n- PHP: used for building web applications and dynamic websites",
    },
    {
      title: "Web Development",
      theme: "summer",
      imagePath: "",
      imageWidth: 0,
      imageHeight: 0,
      description:
        "Web development is the process of creating websites and web applications. It involves using programming languages such as HTML, CSS, and JavaScript to build user interfaces and web functionality. Web development is a broad field that includes front-end development, back-end development, and full-stack development.",
    },
    {
      title: "Mobile Development",
      theme: "summer",
      imagePath: "",
      imageWidth: 0,
      imageHeight: 0,
      description:
        "Mobile development is the process of creating mobile applications for devices such as smartphones and tablets. It involves using programming languages such as Java, Kotlin, Swift, and Objective-C to build native or hybrid apps. Mobile development is a growing field with numerous job opportunities.",
    },
    {
      title: "Data Science",
      theme: "summer",
      imagePath: "",
      imageWidth: 0,
      imageHeight: 0,
      description:
        "Data science is the process of extracting insights and knowledge from data. It involves using programming languages such as Python and R to collect, analyze, and visualize data. Data science has become an essential skill in various industries, including finance, healthcare, and marketing.",
    },
    {
      title: "Career Opportunities in Programming",
      theme: "summer",
      imagePath: "",
      imageWidth: 0,
      imageHeight: 0,
      description:
        "Programming offers a range of career opportunities, including: \n\n- Software developer \n- Web developer \n- Mobile app developer \n- Data analyst \n- Data scientist \n- Cybersecurity specialist \n- Game developer \n- IT consultant \n\nWith the increasing demand for programmers, pursuing a career in programming can be a lucrative and fulfilling choice.",
    },
  ],
};

export type Theme = {
  backgroundColor: string;
  titleColor: string;
  contentColor: string;
};

export const BLACK_THEME: Theme = {
  backgroundColor: "000000",
  titleColor: "FFFFFF",
  contentColor: "B2B2B2",
};

export const WHITE_THEME: Theme = {
  backgroundColor: "FFFFFF",
  titleColor: "000000",
  contentColor: "808080",
};

export const PPTthemes = [
  {
    id: "light",
    title: "Light",
    bg: "bg-white",
    text: "text-black",
    innerBG: "#f2f2f2",
    ring: "ring-blue-600",
  },
  {
    id: "blue-gradient",
    title: "Blue Gradient 1.0",
    bg: "bg-gradient-to-r from-blue-500 to-blue-700",
    text: "text-white",
    innerBG: "#338eff",
    ring: "ring-blue-600",
  },
  {
    id: "dark",
    title: "Black ",
    bg: "bg-black",
    text: "text-white",
    innerBG: "#101010",
    ring: "ring-blue-600",
  },
];

export const containerVariants = {
  visible: {
    scale: 1,
    transition: {
      staggerChildren: 0.3, // delay between each child animation
    },
  },
  hidden: { scale: 0 },
};

export const childVariants = {
  visible: { y: 0, opacity: 1 },
  hidden: { y: 50, opacity: 0 },
};

export const sidebarMenus = [
  {
    id: 21111,
    title: `Text-containing images`,
    icon: mobile,
    path: "/text-image",
    modalDescription: "This is my modal descriptor",
  },
  {
    id: 2,
    title: "Type-based PowerPoint generator",
    icon: ppt,
    path: "/dashboard/powerpoint",
  },
  {
    id: 3,
    title: "Exam Preparation",
    icon: quiz,
    path: "/dashboard/exam",
  },
  {
    id: 4,
    title: "Text Craft and Essays",
    icon: assistant,
    path: "/dashboard/essays",
  },
  {
    id: 5,
    title: "Automated Summarization",
    icon: book,
    path: "/dashboard/summarization",
  },
  {
    id: 73,
    title: "Automated Citation Generation",
    icon: generator,
    path: "/dashboard",
  },
];

export const styles = {
  boxWidth: "xl:max-w-[1280px] w-full",

  heading2:
    "font-poppins font-semibold xs:text-[48px] text-[40px] text-white xs:leading-[76.8px] leading-[66.8px] w-full",
  paragraph:
    "font-poppins font-normal text-dimWhite text-[18px] leading-[30.8px]",

  flexCenter: "flex justify-center items-center",
  flexStart: "flex justify-center items-start",

  paddingX: "sm:px-16 px-6",
  paddingY: "sm:py-16 py-6",
  padding: "sm:px-16 px-6 sm:py-12 py-4",

  marginX: "sm:mx-16 mx-6",
  marginY: "sm:my-16 my-6",
};

export const features = [
  {
    id: "feature-1",
    icon: calander,
    title: "3 day Trial",
    content:
      "You can try out our services for 3 days before you decide to subscribe. You don't have to make any payments or give any information to try it out.",
  },
  {
    id: "feature-2",
    icon: mobilePhone,
    title: "Mobile APP",
    content:
      "If you are a mobile user, you can use our mobile app to access our software. You can download it from the app store and apple play.",
  },
  {
    id: "feature-3",
    icon: quality,
    title: "High-Quality",
    content:
      "We are offering high quality features and services. We are working hard to make sure that you are satisfied with us. You can even synchronize your phone with your computer and use your phone to take picture of the questions from the paper.",
  },
];

export const featuresTextImage = [
  {
    id: "feature-1",
    icon: mobile,
    title: "Upload Image & Get Answer right away",
    content:
      "You can upload images of your questions and get answers right away. You can also upload images of your notes and get them converted to text. ",
  },
  {
    id: "feature-2",
    icon: mobilePhone,
    title: "Connect your phone to conversations",
    content:
      "You can connect your phone's images to a conversation on your computer. You can also connect your phone's camera to your computer and take pictures of your questions from the paper.",
  },
  {
    id: "feature-4",
    icon: conversation,
    title: "Unlimited Conversation creation",
    content:
      "You can organize your questions into conversations and create as many conversations as you want. You can come back to them later and continue working on them.",
  },
  {
    id: "feature-5",
    icon: fast,
    title: "Fast Response Time",
    content:
      "You can get answers to your questions within seconds. You can get answers faster if you have premium subscription. And something else here which fills the content.",
  },
];

export const featuresExams = [
  {
    id: "feature-1",
    icon: keyboard,
    title: "Get a Quiz on Any Topic Instantly",
    content:
      "Want to level up your knowledge? Type in any topic and instantly get a quiz on the subject! With just a few seconds of practice, you'll be well on your way to becoming an expert.",
  },
  {
    id: "feature-2",
    icon: specific,
    title: "Customized Quizzes Just for You",
    content:
      " Make Your Quizzes as Specific as Possible by Providing More Information and Specifying the Types of Questions You Want to Answer!",
  },
  {
    id: "feature-55",
    icon: book,
    title: "Your Quizzes, Your Way",
    content:
      "Our Platform Allows You to Easily Access and Continue Working on Your Quizzes Whenever You Want. And if You Want to Share Them with Others, You Can Do That Too!",
  },
  {
    id: "feature-444",
    icon: fast,
    title: "Fast Creation Time",
    content:
      "Whether you're looking to brush up on your knowledge or challenge yourself with a new topic, our quiz generator has got you covered. Simply create a quiz in seconds and delete it just as quickly if you need to adjust your approach.",
  },
];

export const essayTestBody = `Empathy and Interpersonal Relationships:
Empathy plays a fundamental role in fostering healthy and meaningful connections between individuals. By stepping into someone else's shoes, we gain insights into their experiences, emotions, and perspectives. This understanding helps build trust, strengthens bonds, and promotes effective communication. Empathy allows us to respond to others with kindness, compassion, and respect, facilitating the development of supportive relationships. Whether in personal or professional settings, empathy enables us to navigate conflicts, resolve differences, and foster cooperation.

Empathy and Societal Cohesion:
In a world marked by divisions, empathy holds the power to heal wounds and bridge gaps between various social groups. By recognizing and appreciating the unique struggles and experiences of marginalized communities, individuals can challenge biases and discrimination. Empathy fosters inclusivity by encouraging people to listen, learn, and empathize with others' perspectives. Through empathy, we can create spaces where everyone feels valued, respected, and understood, leading to a more cohesive and harmonious society.

Empathy and Global Cooperation:
On a global scale, empathy is crucial for promoting understanding and cooperation among nations. By acknowledging the challenges faced by different countries and cultures, empathy paves the way for diplomatic dialogues and peaceful resolutions. Empathetic leaders are more likely to seek common ground, build alliances, and engage in collaborative efforts to address global issues such as climate change, poverty, and conflict. Empathy can help transcend political, cultural, and religious differences, fostering a sense of shared humanity and promoting a collective responsibility for the well-being of our planet.

Nurturing Empathy:
While empathy is a natural human trait, it can be nurtured and developed through conscious efforts. Education systems should emphasize the importance of empathy, incorporating it into curricula and teaching methods. Encouraging diverse perspectives, fostering open discussions, and promoting active listening are effective ways to cultivate empathy among individuals. Additionally, practicing self-empathy, understanding our own emotions, and being mindful of our biases can enhance our ability to empathize with others.`;

export const featuresEssays = [
  {
    id: "feature-1",
    icon: keyboard,
    title: "Write an essay about anything",
    content:
      "Want to level up your knowledge? Type in any topic and instantly get a quiz on the subject! With just a few seconds of practice, you'll be well on your way to becoming an expert.",
  },
  {
    id: "feature-2",
    icon: specific,
    title: "Craft a Text document about anything",
    content: "Create a text document about literally anything that you wish",
  },
  {
    id: "feature-55",
    icon: book,
    title: "Your Quizzes, Your Way",
    content:
      "Our Platform Allows You to Easily Access and Continue Working on Your Quizzes Whenever You Want. And if You Want to Share Them with Others, You Can Do That Too!",
  },
  {
    id: "feature-444",
    icon: fast,
    title: "Fast Creation Time",
    content:
      "Whether you're looking to brush up on your knowledge or challenge yourself with a new topic, our quiz generator has got you covered. Simply create a quiz in seconds and delete it just as quickly if you need to adjust your approach.",
  },
];

export const layout = {
  section: `flex md:flex-row flex-col ${styles.paddingY}`,
  sectionReverse: `flex md:flex-row flex-col-reverse ${styles.paddingY}`,

  sectionImgReverse: `flex-1 flex ${styles.flexCenter} md:mr-10 mr-0 md:mt-0 mt-10 relative`,
  sectionImg: `flex-1 flex ${styles.flexCenter} md:ml-10 ml-0 md:mt-0 mt-10 relative`,

  sectionInfo: `flex-1 ${styles.flexStart} flex-col`,
};

export const footerLinks = [
  {
    title: "Useful Links",
    links: [
      {
        name: "Content",
        link: "https://www.hoobank.com/content/",
      },
      {
        name: "How it Works",
        link: "https://www.hoobank.com/how-it-works/",
      },
      {
        name: "Create",
        link: "https://www.hoobank.com/create/",
      },
      {
        name: "Explore",
        link: "https://www.hoobank.com/explore/",
      },
      {
        name: "Terms & Services",
        link: "https://www.hoobank.com/terms-and-services/",
      },
    ],
  },
  {
    title: "Community",
    links: [
      {
        name: "Help Center",
        link: "https://www.hoobank.com/help-center/",
      },
      {
        name: "Partners",
        link: "https://www.hoobank.com/partners/",
      },
      {
        name: "Suggestions",
        link: "https://www.hoobank.com/suggestions/",
      },
      {
        name: "Blog",
        link: "https://www.hoobank.com/blog/",
      },
      {
        name: "Newsletters",
        link: "https://www.hoobank.com/newsletters/",
      },
    ],
  },
  {
    title: "Partner",
    links: [
      {
        name: "Our Partner",
        link: "https://www.hoobank.com/our-partner/",
      },
      {
        name: "Become a Partner",
        link: "https://www.hoobank.com/become-a-partner/",
      },
    ],
  },
];

export const socialMedia = [
  {
    id: "social-media-1",
    icon: instagram,
    link: "https://www.instagram.com/",
  },
  {
    id: "social-media-2",
    icon: facebook,
    link: "https://www.facebook.com/",
  },
  {
    id: "social-media-3",
    icon: twitter,
    link: "https://www.twitter.com/",
  },
  {
    id: "social-media-4",
    icon: linkedin,
    link: "https://www.linkedin.com/",
  },
];

export const stats = [
  {
    id: "stats-1",
    title: "User Active",
    value: "3800+",
  },
  {
    id: "stats-2",
    title: "Something",
    value: "230+",
  },
  {
    id: "stats-3",
    title: "Subscription",
    value: "2000+",
  },
];
