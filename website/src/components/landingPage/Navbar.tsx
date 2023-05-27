import { useState } from "react";

import { logo, close, menu } from "../../assets";
import { motion } from "framer-motion";

import React from "react";
import Image from "next/image";
import { navLinks } from "@/utils/constants";

function Navbar() {
  const [active, setActive] = useState("Home");
  const [toggle, setToggle] = useState(false);

  return (
    <motion.div>
      <motion.nav
        animate={{ opacity: [0, 1], y: [200, 0] }}
        transition={{ duration: 0.4 }}
        className="w-full flex py-6 justify-between items-center navbar"
      >
        {/* <Image src={logo} alt="studentAI" className="w-[140px] h-[35px]" /> */}

        <ul className="list-none sm:flex hidden justify-end items-center flex-1">
          {navLinks.map((nav, index) => (
            <li
              key={nav.id}
              className={`font-poppins font-normal cursor-pointer text-[16px] ${
                active === nav.title ? "text-white" : "text-dimWhite"
              } ${index === navLinks.length - 1 ? "mr-0" : "mr-10"}`}
              onClick={() => setActive(nav.title)}
            >
              <a href={`#${nav.id}`}>{nav.title}</a>
            </li>
          ))}
        </ul>

        <div className="flex justify-center">
          <motion.div
            whileHover={{
              scale: 1.05,
              transition: { duration: 0.4 },
            }}
            className="sm:hidden flex flex-1 justify-end items-center"
          >
            <Image
              src={toggle ? close : menu}
              alt="menu"
              className="w-[28px] h-[28px] object-contain"
              onClick={() => setToggle(!toggle)}
            />

            <motion.div
              className={`${
                !toggle ? "hidden" : "flex"
              } p-6 bg-red absolute top-20 right-0 mx-4 my-2 min-w-[140px] rounded-xl sidebar`}
            >
              <ul className="list-none flex justify-end items-start flex-1 flex-col">
                {navLinks.map((nav, index) => (
                  <li
                    key={nav.id}
                    className={`font-poppins font-medium cursor-pointer text-[16px] ${
                      active === nav.title ? "text-white" : "text-dimWhite"
                    } ${index === navLinks.length - 1 ? "mb-0" : "mb-4"}`}
                    onClick={() => setActive(nav.title)}
                  >
                    <a href={`#${nav.id}`}>{nav.title}</a>
                  </li>
                ))}
              </ul>
            </motion.div>
          </motion.div>
        </div>
      </motion.nav>
    </motion.div>
  );
}

export default Navbar;
