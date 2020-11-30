import React from 'react';
import {
  DashboardOutlined,
  DeploymentUnitOutlined,
  ScheduleOutlined,
  CalendarOutlined,
  FormOutlined,
  GlobalOutlined,
  UserOutlined,
  SettingOutlined,
  LogoutOutlined,
  ContainerOutlined
} from '@ant-design/icons';

export const links = [
  {
    title: 'Dashboard',
    key: '/',
    icon: <DashboardOutlined />,
  },
  {
    items: [
      {
        key: 'dashboard',
        title: 'Dashboard',
      },
    ],
  },
  {
    title: 'Status Updates',
    key: 'status-updates',
    icon: <ScheduleOutlined />,
    items: [
      {
        key: 'dashboard',
        title: 'Dashboard',
      },
      {
        key: 'messages',
        title: 'Messages',
      },
      {
        key: 'stats',
        title: 'Stats',
      },
    ],
  },
  {
    title: 'Events',
    key: 'events',
    icon: <GlobalOutlined />,
    items: [
      {
        key: 'check-in',
        title: 'QR Scanner',
      },
    ],
  },
  {
    title: 'Account',
    key: 'account',
    icon: <UserOutlined />,
    items: [
      {
        key: 'profile',
        title: 'My Profile',
      },
      {
        key: 'settings',
        title: 'Settings',
      },
    ],
  },
  {
    title: 'Admin',
    key: 'admin',
    icon: <UserOutlined />,
    adminExclusive: true,
    items: [
      {
        key: 'manage-users',
        title: 'Manage Users',
      },
    ],
  },
  {
    title: 'Settings',
    key: 'settings',
    icon: <SettingOutlined />,
    items: [
      {
        key: 'general',
        title: 'General Settings',
      },
      {
        key: 'privacy',
        title: 'Privacy',
      },
      {
        key: 'appearance',
        title: 'Appearance',
      },
      {
        key: 'notifications',
        title: 'Notifications',
      },
    ],
  },
  {
    title: 'Logout',
    key: 'logout',
    icon: <LogoutOutlined />,
  },
];
