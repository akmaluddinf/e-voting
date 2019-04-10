--
-- PostgreSQL database dump
--

-- Dumped from database version 10.7
-- Dumped by pg_dump version 10.7

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: dpr; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dpr (
    no_urut integer NOT NULL,
    nama character varying(100) NOT NULL
);


ALTER TABLE public.dpr OWNER TO postgres;

--
-- Name: presiden; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.presiden (
    no_urut integer NOT NULL,
    nama character varying(100) NOT NULL
);


ALTER TABLE public.presiden OWNER TO postgres;

--
-- Name: voter; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.voter (
    no_ktp integer NOT NULL,
    nama character varying(100) NOT NULL,
    password character varying(100) NOT NULL,
    address character varying(100) NOT NULL,
    pilihan_presiden integer,
    pilihan_dpr integer
);


ALTER TABLE public.voter OWNER TO postgres;

--
-- Data for Name: dpr; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dpr (no_urut, nama) FROM stdin;
1	adit
2	imam
3	ipon
4	fasya
\.


--
-- Data for Name: presiden; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.presiden (no_urut, nama) FROM stdin;
1	jokowi
2	prabowo
\.


--
-- Data for Name: voter; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.voter (no_ktp, nama, password, address, pilihan_presiden, pilihan_dpr) FROM stdin;
1	akmal	tes123	bandung	\N	\N
2	firman	tes123	majalengka	\N	\N
\.


--
-- Name: dpr dpr_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dpr
    ADD CONSTRAINT dpr_pkey PRIMARY KEY (no_urut);


--
-- Name: presiden presiden_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.presiden
    ADD CONSTRAINT presiden_pkey PRIMARY KEY (no_urut);


--
-- Name: voter voter_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voter
    ADD CONSTRAINT voter_pkey PRIMARY KEY (no_ktp);


--
-- Name: voter voter_pilihan_dpr_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voter
    ADD CONSTRAINT voter_pilihan_dpr_fkey FOREIGN KEY (pilihan_dpr) REFERENCES public.dpr(no_urut);


--
-- Name: voter voter_pilihan_presiden_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voter
    ADD CONSTRAINT voter_pilihan_presiden_fkey FOREIGN KEY (pilihan_presiden) REFERENCES public.presiden(no_urut);


--
-- PostgreSQL database dump complete
--

