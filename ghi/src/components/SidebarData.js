import React from 'react';
import * as AiIcons from "react-icons/ai";

export const SidebarData = [
  {
    title: "Home",
    path: "/",
    icons: <AiIcons.AiFillHome />,
    cName: "nav-text",
  },
  {
    title: "Chat",
    path: "/chat",
    icons: <AiIcons.AiFillContacts />,
    cName: "nav-text",
  },
  {
    title: "Accounts",
    path: "/accounts",
    icons: <AiIcons.AiOutlineUser />,
    cName: "nav-text",
  },
];
