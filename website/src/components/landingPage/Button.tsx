import React from "react";
import { motion } from "framer-motion";
import { useRouter } from "next/router";
import { useMediaQuery } from "react-responsive";

const Button = ({
  styles,
  text,
  wFull,
}: {
  styles: any;
  text?: string;
  wFull?: boolean;
}) => {
  const router = useRouter();
  const sm = useMediaQuery({
    query: "(max-width: 720px) and (max-height: 600px)",
  });

  return (
    <motion.button
      whileHover={{ scale: 1.05 }}
      whileTap={{ scale: 1 }}
      type="button"
      onClick={() => (text !== "" ? "" : router.push("/auth/login"))}
      className={`py-4 ${
        sm ? "text-[16px]" : "text-[17px]"
      } px-6 font-poppins font-medium ${wFull ? "w-full " : ""} ${
        sm && "text-xs"
      } text-white bg-blue-gradient rounded-[10px] outline-none ${styles}`}
    >
      {!text ? "Get Started" : text}
    </motion.button>
  );
};

export default Button;
