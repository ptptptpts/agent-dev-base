# Professional TypeScript & React Development Guidelines

## Modern Tech Stack
- **Framework**: Next.js 14/15 with **App Router** (Server Components by default).
- **Validation**: Use **Zod** for schema validation (API responses, Form data, Environment variables).
- **Icons**: Use `lucide-react` for consistent, lightweight iconography.

## State Management Strategy
- **Server State**: Use **TanStack Query (React Query)** for all asynchronous data fetching, caching, and synchronization.
- **Client State**: Use **Zustand** for lightweight, global client-side state. Follow the "Slice Pattern" for large stores.

## Component Architecture
- **Composition**: Prefer composition over large, complex prop-drilling.
- **shadcn/ui**: Use `shadcn/ui` components as the foundation. Extend them with Tailwind CSS as needed.
- **Hooks**: Extract complex logic into custom hooks (e.g., `use-task-logic.ts`).

## Type Safety & DX
- **No `any`**: Strictly enforce no `any` policy. Use `unknown` or proper generics.
- **API Types**: Auto-generate or strictly define types for all API interactions to ensure end-to-end safety.
- **Performance**: Minimize `use client` directives. Use `useMemo` and `useCallback` only when profiling indicates a need.
